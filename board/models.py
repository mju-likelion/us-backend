from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # 1 중고거래, 2 물물교환, 3 리뷰, 4 꿀팁  
    board_type = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="board/post/%Y/%m/%d")
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="like")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title