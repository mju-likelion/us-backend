from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Post

@api_view(['GET']) #GET 요청인지 검증
@permission_classes((IsAuthenticated, )) #권한 체크/ 로그인했는지
@authentication_classes((JSONWebTokenAuthentication,)) # JWT 토큰 확인 / 이상있으면 에러
def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")