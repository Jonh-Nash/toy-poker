from django.urls import path
from .views import signupfunc

urlpatterns = [
    #path('', ),
    #path('', include('poker.urls')),
    path('signup/', signupfunc)
]
