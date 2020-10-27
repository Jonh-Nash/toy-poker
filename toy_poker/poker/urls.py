from django.urls import path
from .views import signupfunc, loginfunc

urlpatterns = [
    #path('', ),
    #path('', include('poker.urls')),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
]
