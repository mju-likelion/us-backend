from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="login"),
    path("token/", obtain_jwt_token),
    path("token/refresh/", refresh_jwt_token),
    path("token/verify/", verify_jwt_token),
    path("userlist/", views.userList.as_view(), name="userlist"),
]
