from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views

app_name = 'board'

urlpatterns = [
    path('',views.posts, name='posts'),
    path('list/',views.postList, name='postList'),
    path('add/', views.PostView.as_view(), name="login"),
    path('tip/',views.tipPostList, name='tipPostList'),
    path('review/',views.reviewPostList, name='reviewPostList'),
    # path("signup/", views.SignupView.as_view(), name="login"),
    # path("token/", obtain_jwt_token),
    # path("token/refresh/", refresh_jwt_token),
    # path("token/verify/", verify_jwt_token),
]
