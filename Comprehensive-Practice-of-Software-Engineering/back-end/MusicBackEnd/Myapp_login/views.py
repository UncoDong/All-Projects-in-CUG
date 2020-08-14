from django.shortcuts import render
from Myapp_login.models import User
from django.http import HttpResponseRedirect
def register(request):
    context = {}
    context['stat'] = 'regist'
    if 'user' and 'password' in request.POST:
        user_name = request.POST['user']
        password = request.POST['password']
        print('得到',user_name,password)
        user_list = User.objects.filter(name=user_name)
        if len(user_list)== 0:
            print('注册中')
            new_user = User(name=user_name,password=password)
            new_user.save()
            context['user_name'] = user_name
            return render(request,'login.html',context)
        else:
            context['wrong'] = '已存在该用户'
    else:
        context['wrong'] = '请输入数据'

    return render(request,'register.html',context)

def login(request):
    print(request.POST)
    context = {}
    #设置状态
    context['stat'] = 'login'
    if 'user' and 'password' in request.POST:  #如果有数据提交了的话
        #传递数据
        user_name = request.POST['user']
        print('用户',user_name)
        # 查找用户
        user_list = User.objects.filter(name=user_name)
        if len(user_list) == 0:
            context['wrong'] = '没有该用户'
        else:
            #去数据库查询user
            user = user_list[0]
            print('应有的密码',user.password)
            if request.POST['password'] == user.password:       #对比数据
                context['titl1'] = 'success'
                context['user_name'] = user_name
                request.session['user'] = user_name
                #成功后跳转主页
                return render(request, 'home.html', context)
            else:               #对比失败，修改状态
                context['wrong'] = '用户名或密码❌'
    else:
        context['wrong'] = '请输入数据'
    #失败停留在原来的界面

    return render(request,'login.html',context)

# 判断登录状态
def login_state(request):
    context = {}
    context['user_name'] = request.session.get('user')
    return render(request, 'status_intest.html', context)

# 登出
def logout(request):
    context = {}
    request.session.flush()
    context['user_name'] = request.session.get('user')

    return HttpResponseRedirect('/Myapp_runweb/home/')


