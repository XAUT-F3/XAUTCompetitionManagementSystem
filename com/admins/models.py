from django.db import models
# from django_summernote.fields import SummernoteTextField
from django.core import serializers


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=20)  # 文章标题
    author = models.CharField(max_length=10)  # 文章作者
    type = models.CharField(max_length=10)  # 文章类型
    # time = models.DateTimeField(format('%Y-%m-%d %H:%M:%S'))
    time = models.DateTimeField()
    # context = SummernoteTextField()  # 文章内容
    context = models.TextField()  # 文章内容

    class Meta:
        db_table = 'news'
