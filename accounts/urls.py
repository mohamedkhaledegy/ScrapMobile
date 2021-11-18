from django.urls import path

from accounts.models import Profile
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup',views.signup,name='signup') ,
    path('profile',views.profile,name='profile') ,
]
