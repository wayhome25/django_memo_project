from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Memos
from .forms import PostForm

# from HTMLParser import HTMLParser


def index(request):
    if request.method == "POST":
        target = Memos.objects.get(pk = {{memo.pk}}) # 수정필요
        target.delete()
        memos = Memos.objects.all()
        return render(request, 'memo_app/default.html', {'memos' : memos})
    else:
        memos = Memos.objects.all()
        return render(request, 'memo_app/default.html', {'memos' : memos})

def post(request):
    if request.method == "POST":
        #저장
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        #입력
        form = PostForm()
        return render(request, 'memo_app/form.html',{'form': form})

def modify(request, memokey):
    if request.method == "POST":
        #수정 저장
        memo = Memos.objects.get(pk = memokey)
        form = PostForm(request.POST, instance=memo)
        if form.is_valid():
             form.save()
             return redirect('index')
    else:
        #수정 입력
        memo = Memos.objects.get(pk = memokey)
        form = PostForm(instance = memo)
        return render(request, 'memo_app/modify.html', {'memo' : memo, 'form' : form})

def delete(request, memokey):
    memo = Memos.objects.get(pk = memokey)
    memo.delete()
    return redirect('index')
