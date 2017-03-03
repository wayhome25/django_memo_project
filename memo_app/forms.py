from django import forms
from .models import Memos
# 모델 클래스 Memos로 부터 데이터를 입력 받을 폼을 작성한다.

class PostForm(forms.ModelForm):
    class Meta:
        model = Memos
        fields = ['title', 'name', 'text', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'180자 이내로 입력 가능합니다.'}),
            'priority': forms.CheckboxInput(attrs={'type' : 'checkbox'}),
        }
        labels = {
            'title': '제목',
            'name': '이름',
            'text': '내용',
            'priority': '중요',
        }
