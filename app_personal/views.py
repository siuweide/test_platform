from django.contrib import auth
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            response = redirect('/project/list/')
            response.set_cookie('user', username, 3600)
            return response
        else:
            error_message = '账号或密码错误'
            return render(request, 'login.html', {
                'error_message':error_message
            })


def logout(request):
    auth.logout(request)
    return redirect('/login/')