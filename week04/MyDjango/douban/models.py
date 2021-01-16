from django.db import models
from datetime import datetime

# Create your models here.
class Comment(models.Model):
    # 自增id
    movie_name = models.CharField(verbose_name='电影名', max_length=50)
    nickname = models.CharField(verbose_name='昵称', max_length=100)
    rate = models.CharField(verbose_name='评分', max_length=5)
    content = models.CharField(verbose_name='评论内容', max_length=500)
    comment_date = models.DateTimeField(verbose_name='评论日期')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=datetime.now().replace(microsecond=0))
    update_at =  models.DateTimeField(verbose_name='更新时间', auto_now=datetime.now().replace(microsecond=0))


class Comment_test(models.Model):
    # 自增id
    movie_name = models.CharField(verbose_name='电影名', max_length=50)
    nickname = models.CharField(verbose_name='昵称', max_length=100)
    rate = models.CharField(verbose_name='评分', max_length=5)
    content = models.CharField(verbose_name='评论内容', max_length=1000)
    comment_date = models.DateTimeField(verbose_name='评论日期')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=datetime.now().replace(microsecond=0))
    update_at =  models.DateTimeField(verbose_name='更新时间', auto_now=datetime.now().replace(microsecond=0))