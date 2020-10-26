from django.shortcuts import render

def signupfunc(request):
    # actionで遷移先を空、つまり自ページにする。
    # 自分に送りつけてからページ遷移する処理をこちらで書く
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        return render(request, 'signup.html', {'some': 200}) 

    return render(request, 'signup.html', {'some': 200}) 
