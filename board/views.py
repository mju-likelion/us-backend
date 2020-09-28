from django.shortcuts import render
from django.core import serializers

from rest_framework.response import Response
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.generics import CreateAPIView

from .serializers import PostListSerializer, AddPostSerializer

from .models import Post

@api_view(['GET']) #GET 요청인지 검증
@permission_classes((IsAuthenticated, )) #권한 체크/ 로그인했는지
@authentication_classes((JSONWebTokenAuthentication,)) # JWT 토큰 확인 / 이상있으면 에러
def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")

@api_view(['GET']) #GET 요청인지 검증
@permission_classes((AllowAny, )) # 권한체크 / 메인 화면에 나오는 것이기때문에 누구나 가능
def postList(request):
    serializer = PostListSerializer(Post.objects.all(),many=True)
    return Response(serializer.data)
    # posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    # post_list = serializers.serialize('json', posts)
    # return HttpResponse(post_list, content_type="text/json-comment-filtered")

@api_view(['GET'])
@permission_classes((AllowAny, ))
def reviewPostList(request):
    serializer = PostListSerializer(Post.objects.filter(board_type=3),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def tipPostList(request):
    serializer = PostListSerializer(Post.objects.filter(board_type=4),many=True)
    return Response(serializer.data)

@permission_classes((AllowAny, )) # 권한체크 / 회원가입 전이기 때문에 누구나 접근가능
class PostView(CreateAPIView):
    serializer_class = AddPostSerializer


# @api_view(['GET'])
# @permission_classes((AllowAny, ))
