from django.urls import path
from .views import loginUser, logOutUser, signinUser

urlpatterns = [
    path("signup/",signinUser, name="signup"),
    path("login/",loginUser , name="login"),
    path("logout/",logOutUser , name="logout"),
]
