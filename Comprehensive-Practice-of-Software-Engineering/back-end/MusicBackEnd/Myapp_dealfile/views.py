from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
import os
import time
import librosa
import numpy as np
# Create your views here.
from django.template import loader
# Create your views here.
import chardet     # 获取上传文件编码格式
from Myapp_covert2musicscore.utils.music21tools import *
from Myapp_dealfile.utils.util import *

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import os
from django.http import HttpResponse,StreamingHttpResponse
from django.conf import settings
from django.utils.http import urlquote
from django.views import generic
'''
Summary:
    展示文件上传的首页
Return:
    首页的html
'''
def show_uploadfile_index(request):
    return render(request, 'uploads.html', context)

'''
Summary:
    上传文件的功能
Return:
    上传讯息
'''
def upload_file(request):
    print(request)
    if request.method == 'GET':
        return HttpResponse('就这？')
    if request.method == 'POST':
        print(request.FILES)
        my_file = request.FILES.get("my_file", None)
        print(str(my_file))
        file_name = str(my_file).split('.')[0]
        print (my_file, '++++++++++++++++++++++')
        if not my_file:
            return HttpResponseRedirect('/Myapp_runweb/file2musicscore/')
        # 上传文件的目录
        filpath = os.path.join("./Myapp_dealfile/static/uploadfiles", my_file.name)
        destination = open(filpath, 'wb+')
        for chunk in my_file.chunks():
            destination.write(chunk)
            print(destination, '----------------------')
        destination.close()
        print('上传结束')


        user_name = request.session.get('user')
        context = {}
        context['user_name'] = request.session.get('user')
        if context['user_name']:
            login_or_logout = "/Myapp_login/logout"
        else:
            login_or_logout = "/Myapp_login/login"
        context['login_or_logout'] = login_or_logout


        # 这里进行转换
        musicname,wavname = method_fft(filpath,user_name,file_name)
        context['musicname'] = musicname
        context['wavname'] = wavname
        return render(request, 'preview.html', context)
        #return render(request, 'test_show_musicscore_pic.html', {'musicname':musicname+'-1.png'})

'''
Summary:
    下载文件的功能
Return:
    就是一个下载的弹窗
'''
def download_file(request,filename):
    # if request.method == 'Get':
    # filename = request.GET.get('file')
    filepath = os.path.join("./Myapp_dealfile/static/wavfiles", filename)
    print(filepath)
    fp = open(filepath, 'rb')
    response = StreamingHttpResponse(fp)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % (urlquote(filename))

    return response
    fp.close()

'''
Summary:
    将文件信息转换成流
Return:
    流
'''
def musicfile_fft_to_stream(data,num):
    s = stream.Score(id='mainScore')
    measurenum = 0
    midstream = stream.Measure(number=measurenum/4)
    for i in range(len(data)):
        length = int(num[i])
        if length > 10:
            mynote = note.Note(data[i])
            mynote.quarterLength = length/30
            midstream.append(mynote)
            measurenum+=1
            if measurenum%4 == 0:
                s.append(midstream)
                midstream = stream.Measure(number=measurenum/4)
    return s

'''
Summary:
    fft方法分析文件
return:
    谱子图片
'''
def method_fft(filname,user_name,music_name):
    # 处理音频
    y,rate=librosa.load(filname,sr=44100)
    fft=librosa.stft(y,n_fft=1024*2)
    D=librosa.amplitude_to_db(abs(fft),ref=np.max)
    D=D+80
    data=music_to_note(D,rate/2)
    data,num=get_note_and_num(data)
    # 文件信息转换成流
    s = musicfile_fft_to_stream(data,num)

    s.insert(0, metadata.Metadata())
    s.metadata.title = music_name
    s.metadata.composer = user_name

    musicname = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    print('音乐名字',musicname)

    png_filname = write_xml_and_get_png(s)
    wav_filname = write_midi_and_get_wav(s)
    #print(wav_filname)
    return png_filname+'-1.png',wav_filname+'.wav'



'''
Summary:
    处理文件
Return:
    一个谱子的图片
'''
def deal_file(request):
    ''''''


