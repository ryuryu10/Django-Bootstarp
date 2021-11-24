from django.db import models
from django.db.models.base import Model

class Post(models.Model):
    title = models.CharField(max_length=30) #CharFiedl클래스의 최대길이는 30
    content = models.TextField() #TextField / 문자열의 길이 제한이 없음

    created_at = models.DateTimeField(auto_now_add=True) #월,일,시,분,초까지 기록할수 있는 필드
    updateed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}' #pk는 각 레코드에 대한 고유값이다
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}'