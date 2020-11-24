from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import UserInfo
from django.contrib.auth.decorators import login_required
import random

def bot_actions(bot_posi, BTN_card, BB_card):
    if bot_posi == "BTN":
        if BTN_card == "A":
            bot_action = "bet"
        if BTN_card == "Q":
            bot_action = random.choice(["check", "bet"])
    if bot_posi == "BB":
        bot_action = random.choice(["call", "fold"])

    return bot_action

def cardDeal(AQlist):
    BTN_card = AQlist.pop()
    BB_card = "K"
    return BTN_card, BB_card, AQlist

def takeChipWinner(winner, player_posi, action_player, action_opp):
    # posi is BB
    if player_posi == "BTN":
        if action_player == "check":
            if winner == "BTN":
                return 1
            else:
                return -1
        elif action_opp == "fold":
            return 1
        elif action_opp == "call":
            if winner == "BTN":
                return 3
            else:
             return -3

    if player_posi == "BB":
        if action_opp == "check":
            if winner == "BB":
                return 1
            else:
                return -1
        elif action_player == "fold":
            return -1
        elif action_player == "call":
            if winner == "BB":
                return 3
            else:
                return -3

def cardOpen(BTN_card, BB_card):
    card_rank = ["Q", "K", "A"]
    BTN_card_rank = card_rank.index(BTN_card)
    BB_card_rank = card_rank.index(BB_card)
    if BTN_card_rank > BB_card_rank:
        winner = "BTN"
    else:
        winner = "BB"
    return winner

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
    user_info = UserInfo.objects.filter(user=request.user)
    # カードを配る
    opp_card = "K"
    player_card = "Q"

    if request.method == 'GET':
        content = {
            'user' : user_info[0].user,
            'turn' : user_info[0].turn,
            'tokuten' : user_info[0].tokuten,
        }
        return render(request, 'poker_btn.html', content)

    if request.method == 'POST':
        # 結果から獲得ポイントを出し、フラグを立てる
        action_player = request.POST['action']
        action_opp = bot_actions("BB", player_card, opp_card)
        winner = cardOpen(player_card, opp_card)
        point = takeChipWinner(winner, "BTN", action_player, action_opp)
        card_flag = True
        content = {
            'user' : user_info[0].user,
            'turn' : user_info[0].turn,
            'tokuten' : user_info[0].tokuten,
            'action' : action_player,
            'action_opp': action_opp,
            'card_flag': card_flag,
            'point' : point,
        }
        return render(request, 'poker_btn.html', content)

    return render(request, 'poker_btn.html')
    
@login_required
def pokerbbfunc(request):
    # カードを配る
    user_info = UserInfo.objects.filter(user=request.user)
    player_card = "K"
    opp_card = "A"

    if request.method == 'GET':
        content = {
            'user' : user_info[0].user,
            'turn' : user_info[0].turn,
            'tokuten' : user_info[0].tokuten,
            'action_opp' : 'bet',
        }
        return render(request, 'poker_bb.html', content)
    if request.method == 'POST':
        # 結果から獲得ポイントを出し、フラグを立てる
        action_player = request.POST['action']
        action_opp = bot_actions("BTN", opp_card, player_card)
        winner = cardOpen(opp_card, player_card)
        point = takeChipWinner(winner, "BB", action_player, action_opp)
        card_flag = True
        content = {
            'user' : user_info[0].user,
            'turn' : user_info[0].turn,
            'tokuten' : user_info[0].tokuten,
            'action' : action_player,
            'action_opp': action_opp,
            'card_flag': card_flag,
            'point' : point,
        }
        return render(request, 'poker_bb.html', content)

    return render(request, 'poker_btn.html')
    