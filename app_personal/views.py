from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print('进入到else语句')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            print('user校验成功')
            auth.login(request, user)
            return redirect('/project/list/')
        else:
            error_message = '账号或密码错误'
            return render(request, 'login.html', {
                'error_message':error_message
            })

