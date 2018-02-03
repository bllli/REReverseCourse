from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm


def login(request):
    """登录"""
    if request.user.is_authenticated:
        messages.warning(request, '用户 {username}, 你已经登陆'.format(username=request.user.username))
        return redirect('index')
    login_form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if login_form.is_valid():
            user = login_form.get_and_check_user()
            auth.login(request, user)
            messages.success(request, '欢迎回来, {username}'.format(username=request.user.username))
            return redirect('index')
        else:
            messages.error(request, '账号或密码错误')
    return render(request, 'login.html', {
        'login_form': login_form
    })


@login_required
def logout(request):
    """登出"""
    auth.logout(request)
    messages.success(request, '登出成功, Bye~')
    return redirect('index')
