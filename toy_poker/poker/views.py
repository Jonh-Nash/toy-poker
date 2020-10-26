from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):
    # actionで遷移先を空、つまり自ページにする。
    # 自分に送りつけてからページ遷移する処理をこちらで書く
    user2 = User.objects.get(username='sato')
    print(user2)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, '', password)
        return render(request, 'signup.html', {'some': 200}) 

    return render(request, 'signup.html', {'some': 200}) 
