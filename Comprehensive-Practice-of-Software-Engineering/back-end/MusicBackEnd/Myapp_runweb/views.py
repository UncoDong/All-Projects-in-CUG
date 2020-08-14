from django.shortcuts import render
from Myapp_login.models import User,Score
from Myapp_runweb.utils.util import make_user_json,make_all_json
from django.http import HttpResponseRedirect
# Create your views here.
'''
Summary:
    展示主页
Return:
    首页的html
'''
def home(request):
    context = {}
    context['user_name'] = request.session.get('user')
    if context['user_name']:
        login_or_logout = "/Myapp_login/logout"
    else:
        login_or_logout = "/Myapp_login/login"
    context['login_or_logout'] = login_or_logout

    return render(request, 'home.html', context)

'''
Summary:
    展示字符串上传的首页
Return:
    首页的html
'''
def str_to_musicscore(request):
    context = {}
    context['user_name'] = request.session.get('user')
    if context['user_name']:
        login_or_logout = "/Myapp_login/logout"
    else:
        login_or_logout = "/Myapp_login/login"
    context['login_or_logout'] = login_or_logout

    return render(request, 'str2musicscore.html', context)

'''
Summary:
    展示声波图
Return:
    首页的html
'''
def wave_scope(request):
    context = {}
    context['user_name'] = request.session.get('user')
    if context['user_name']:
        login_or_logout = "/Myapp_login/logout"
    else:
        login_or_logout = "/Myapp_login/login"
    context['login_or_logout'] = login_or_logout

    return render(request, 'wavescope.html', context)

'''
Summary:
    展示在线钢琴
Return:
    首页的html
'''
def piano_online(request):
    context = {}
    context['user_name'] = request.session.get('user')
    if context['user_name']:
        login_or_logout = "/Myapp_login/logout"
    else:
        login_or_logout = "/Myapp_login/login"
    context['login_or_logout'] = login_or_logout

    # 每次都要重新制作曲谱
    print(Score.objects.all())
    user_score_list = Score.objects.filter(user_name=request.session.get('user'))
    print('用户',request.session.get('user'))
    print(user_score_list)
    all_score_list = Score.objects.all()
    print(all_score_list)
    #for user_score in user_score_list:
    #    print(user_score)
    make_user_json(user_score_list)

    make_all_json(all_score_list)
    return render(request, 'pianoOnLine.html', context)





'''
Summary:
    展示节拍器
Return:
    首页的html
'''
def metronome(request):
    context = {}
    context['user_name'] = request.session.get('user')
    if context['user_name']:
        login_or_logout = "/Myapp_login/logout"
    else:
        login_or_logout = "/Myapp_login/login"
    context['login_or_logout'] = login_or_logout

    return render(request, 'metronome.html', context)

'''
Summary:
    上传文件
Return:
    首页的html
'''
def file_to_musicscore(request):
    context = {}
    context['user_name'] = request.session.get('user')
    if context['user_name']:
        login_or_logout = "/Myapp_login/logout"
    else:
        login_or_logout = "/Myapp_login/login"
    context['login_or_logout'] = login_or_logout

    return render(request, 'file2musicscore.html', context)

def login(request):
    print(request)
    context = {}
    context['user_name'] = request.session.get('user')
    if context['user_name']:
        login_or_logout = "/Myapp_login/logout"
    else:
        login_or_logout = "/Myapp_login/login"
    context['login_or_logout'] = login_or_logout

    return render(request, 'login.html', context)

def register(request):
    context = {}
    context['user_name'] = request.session.get('user')
    if context['user_name']:
        login_or_logout = "/Myapp_login/logout"
    else:
        login_or_logout = "/Myapp_login/login"
    context['login_or_logout'] = login_or_logout
    return render(request, 'register.html', context)


def del_score(request):
    print('混奥')
    print(request)
    print(request.POST)
    context = {}
    dic_post = eval(request.POST['score_json_delete'])
    print(dic_post)
    score_name =dic_post['score_name']
    user_name =dic_post['user_name']

    find_list = Score.objects.filter(user_name=user_name,score_name=score_name)
    find_list[0].delete()
    return HttpResponseRedirect('/Myapp_runweb/pianoOnLine/')

