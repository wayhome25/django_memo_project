from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Memos
from .forms import PostForm
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, views



# from HTMLParser import HTMLParser

def index(request):
    if request.method == "POST":
        target = Memos.objects.get(pk = {{memo.pk}}) # 수정필요
        target.delete()
        memos = Memos.objects.order_by('-update_date')
        return render(request, 'memo_app/default.html', {'memos' : memos})
    else:
        memos = Memos.objects.order_by('-update_date')
        return render(request, 'memo_app/default.html', {'memos' : memos})

def post(request):
    if request.method == "POST":
        #저장
        form = PostForm(request.POST)
        if form.is_valid():
            memo = form.save(commit = False)
            memo.name_id = User.objects.get(username = request.user.get_username())
            memo.generate()
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
        if memo.name_id == User.objects.get(username = request.user.get_username()):
            memo = Memos.objects.get(pk = memokey)
            form = PostForm(instance = memo)
            return render(request, 'memo_app/modify.html', {'memo' : memo, 'form' : form})
        else:
            return render(request, 'memo_app/warning.html')


def delete(request, memokey):
    memo = Memos.objects.get(pk = memokey)
    if memo.name_id == User.objects.get(username = request.user.get_username()):
        memo.delete()
        return redirect('index')
    else:
        return render(request, 'memo_app/warning.html')

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'memo_app/login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form = UserForm()
        return render(request, 'memo_app/adduser.html', {'form': form})
