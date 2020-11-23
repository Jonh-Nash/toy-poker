from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import UserInfo
from django.contrib.auth.decorators import login_required
import random

def signupfunc(request):
    # actionで遷移先を空、つまり自ページにする。
    # 自分に送りつけてからページ遷移する処理をこちらで書く
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            # make deck
            AQlist = ["A"] * 25 + ["Q"] * 25
            random.shuffle(AQlist)
            deck = "".join(AQlist)
            user_info = UserInfo(user=username2, turn=0, tokuten=0, deck=deck)
            user_info.save()
            return render(request, 'signup.html', {'some': 200}) 

    return render(request, 'signup.html', {'some': 200}) 

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('poker_btn')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required
def pokerbtnfunc(request):
    if request.method == 'GET':
        user_info = UserInfo.objects.filter(user=request.user)
        content = {
            'user' : user_info[0].user,
            'turn' : user_info[0].turn,
            'tokuten' : user_info[0].tokuten,
        }
        return render(request, 'poker_btn.html', content)
    if request.method == 'POST':
        user_info = UserInfo.objects.filter(user=request.user)
        # 対戦相手のアクション
        action_opp = 'call'
        card_flag = True
        content = {
            'user' : user_info[0].user,
            'turn' : user_info[0].turn,
            'tokuten' : user_info[0].tokuten,
            'action' : request.POST['action'],
            'action_opp': action_opp,
            'card_flag': card_flag
        }
        return render(request, 'poker_btn.html', content)

    return render(request, 'poker_btn.html')
    
@login_required
def pokerbbfunc(request):
    if request.method == 'GET':
        user_info = UserInfo.objects.filter(user=request.user)
        content = {
            'user' : user_info[0].user,
            'turn' : user_info[0].turn,
            'tokuten' : user_info[0].tokuten,
            'action_opp' : 'bet',
        }
        return render(request, 'poker_bb.html', content)
    if request.method == 'POST':
        user_info = UserInfo.objects.filter(user=request.user)
        # 対戦相手のアクション
        card_flag = True
        content = {
            'user' : user_info[0].user,
            'turn' : user_info[0].turn,
            'tokuten' : user_info[0].tokuten,
            'action' : request.POST['action'],
            'card_flag': card_flag
        }
        return render(request, 'poker_bb.html', content)

    return render(request, 'poker_btn.html')
    