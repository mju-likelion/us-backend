from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from .serializers import SignupSerializer


#@api_view(['POST']) # POST 요청인지 검증
@permission_classes((AllowAny, )) # 권한체크 / 회원가입 전이기 때문에 누구나 접근가능
class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer

