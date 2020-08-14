from django.shortcuts import render
from django.http.response import HttpResponse
import os
import time
# Create your views here.
from django.template import loader
from Myapp_covert2musicscore.utils.music21tools import *
from django.http import HttpResponseRedirect
from Myapp_login.models import Score
def use_music21(music_str,music_name, user_name):
    pan = False
    print('准备预测')
    for each in music_str:
        if each.isupper() == True:
            pan = True
            break
    # 如果没有大写字母，也就是纯数字
    if pan == False:
        print('纯数字')
        s = musicstr_to_stream(music_str)
    else:
        print('大写字母')
        s = musicstr_char_to_stream(music_str)
    s.insert(0, metadata.Metadata())
    s.metadata.title = music_name
    s.metadata.composer = user_name
    png_filname = write_xml_and_get_png(s)
    wav_filname = write_midi_and_get_wav(s)
    return png_filname+'-1.png',wav_filname+'.wav'


'''
Summary:
    将音乐字符串转换成图片
Return:
    返回转换后的结果
'''
def convert_musicstr_2_pic(request):
    # 如果用户登录了
    if request.method == 'GET':
        print(request.GET)
        music_str = request.GET.get('music_str')
        music_name = "无题"
        print(music_str)
    elif request.method == 'POST':
        music_str = request.POST.get('str-container')
        music_name =request.POST.get('str-scorename')
        print(request.POST)
        print(music_str)
        user_name = request.session.get('user')
        print(user_name)
        # 判断数据库中是否有这个
        que = len(Score.objects.filter(score_name__startswith=music_name,user_name=user_name))
        if que!=0:
            music_name +='_{0}'.format(que)
        musicname,wavname = use_music21(music_str,music_name=music_name,user_name=user_name)
        if request.session.get('user'):
            score = Score()
            # 保存曲谱信息
            #musicpath = "/static/musicpng/"+ musicname
            #wavpath = "/Myapp_dealfile/downloadfile/"+ wavname
            musicpath =  musicname
            wavpath =  wavname
            score.user_name = user_name
            score.png_path = musicpath
            score.wav_path = wavpath
            score.score_name = music_name
            print(score)

            score.save()

    context = {}
    context['user_name'] = request.session.get('user')
    if context['user_name']:
        login_or_logout = "/Myapp_login/logout"
    else:
        login_or_logout = "/Myapp_login/login"
    context['login_or_logout'] = login_or_logout
    context['musicname'] = musicname
    context['wavname'] = wavname
    return render(request, 'preview.html', context)
        # 将字符串放入上下文，以后用
        # return render(request, 'test_show_musicscore_pic.html', {'musicname':musicname+'-1.png'})
    # else:
    #     print('用户还没注册')
    #     return HttpResponseRedirect("/Myapp_login/login/")
    #
    #     #return render(request, 'login.html', {'music_str':music_str})


def show_from_user(request):
    print('输出')

    dic_post = eval(request.POST['score_json_download'])
    print(dic_post)
    musicpath =dic_post['png_url']
    wavpath =dic_post['wav_url']
    return render(request, 'preview2.html', {'musicpath':musicpath,'wavpath':wavpath})


'''
Summary:
    展示字符串上传的首页
Return:
    首页的html
'''
def show_uploadstr_index(request):
    return render(request, 'str2music.html', context)

'''
Summary:
    展示图片(测试用)
Return:
    含有图片的html(测试用)
'''
def test_show_pic(request):
    print('到这里')
    template = loader.get_template('test_show_musicscore_pic.html')
    context = {}
    return HttpResponse(template.render(context, request))





