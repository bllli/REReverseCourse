from django.contrib import auth
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, help_text='请输入您的用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

    def get_and_check_user(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        return user

    def clean(self):
        user = self.get_and_check_user()
        if not user or not user.is_active:
            raise forms.ValidationError('登录失败,账号或密码错误')
