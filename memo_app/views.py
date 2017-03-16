from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from .models import Memos
from .forms import PostForm
from .forms import UserForm
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth import login, views
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST



# from HTMLParser import HTMLParser

@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        memo_id = request.POST.get('pk', None)
        memo = Memos.objects.get(pk = memo_id)

        if memo.likes.filter(id = user.id).exists():
            memo.likes.remove(user)
            message = '좋아요 취소'
        else:
            memo.likes.add(user)
            message = '좋아요!'

    context = {'likes_count' : memo.total_likes, 'message' : message}
    return HttpResponse(json.dumps(context), content_type='application/json')


def index(request):
    sort = request.GET.get('sort','')
    if sort == 'likes':
        memos = Memos.objects.annotate(like_count=Count('likes')).order_by('-like_count', '-update_date')
        return render(request, 'memo_app/index.html', {'memos' : memos})
    elif sort == 'mypost':
        user = request.user
        memos = Memos.objects.filter(name_id = user).order_by('-update_date') #복수를 가져올수 있음
        return render(request, 'memo_app/index.html', {'memos' : memos})
    else:
        memos = Memos.objects.order_by('-update_date')
        return render(request, 'memo_app/index.html', {'memos' : memos})

# 글 입력 및 저장
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

# 글 수정 및 저장
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

# 글 삭제
def delete(request, memokey):
    memo = Memos.objects.get(pk = memokey)
    if memo.name_id == User.objects.get(username = request.user.get_username()):
        memo.delete()
        return redirect('index')

    else:
        return render(request, 'memo_app/warning.html')

# 회원가입
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
