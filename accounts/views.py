from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core import serializers

from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes

#인증관련
from rest_framework.permissions import AllowAny

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from .serializers import SignupSerializer, UserListSerializer

from .models import User

#@api_view(['POST']) # POST 요청인지 검증
@permission_classes((AllowAny, )) # 권한체크 / 회원가입 전이기 때문에 누구나 접근가능
class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer

#@api_view(['GET'])
@permission_classes((AllowAny, ))
class userList(APIView):
    def get(self, request):
        serializer = UserListSerializer(User.objects.filter(is_superuser=0), many=True)
        return Response(serializer.data)
