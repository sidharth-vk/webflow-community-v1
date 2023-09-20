
from django.urls import path
from .views import *


urlpatterns = [
    path('authentication/login',log_in,name="login"),
    path('authentication/register',register_page,name="register_page"),
    path("profile/<pk>",profile_page_output, name="profile_page_output"),
    path("addfriend/<pk>",addfriend, name="addfriend"),
    path("logout",logout_user, name="logout_user"),
] 