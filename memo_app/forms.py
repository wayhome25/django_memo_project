from django import forms
from .models import Memos
# 모델 클래스 Memos로 부터 데이터를 입력 받을 폼을 작성한다.
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Memos
        fields = ['title','text', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'230자 이내로 입력 가능합니다.'}),
            'priority': forms.CheckboxInput(attrs={'type' : 'checkbox'}),
        }
        labels = {
            'title': '제목',
            'text': '내용',
            'priority': '중요',
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': '닉네임',
            'email': '이메일',
            'password': '패스워드'
        }
    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15
