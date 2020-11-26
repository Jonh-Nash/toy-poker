from django.urls import path
from .views import signupfunc, loginfunc, pokerbtnfunc, pokerbbfunc, trainbtnfunc, trainbbfunc

urlpatterns = [
    #path('', ),
    #path('', include('poker.urls')),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('poker_btn/', pokerbtnfunc, name='poker_btn'),
    path('poker_bb/', pokerbbfunc, name='poker_bb'),
    path('train_btn/', trainbtnfunc, name='train_btn'),
    path('train_bb/', trainbbfunc, name='train_bb'),
]
