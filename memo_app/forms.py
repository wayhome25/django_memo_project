from django import forms
from .models import Memos
# 모델 클래스 Memos로 부터 데이터를 입력 받을 폼을 작성한다.

class PostForm(forms.ModelForm):
    class Meta:
        model = Memos
        fields = ('title', 'name', 'text', 'priority')
