from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, blank=False)
    password = models.CharField(verbose_name='密码', max_length=32)


class ProjectInfo(models.Model):
    pro_name = models.CharField(verbose_name='项目名', max_length=100, unique=True)
    pro_intro = models.CharField(verbose_name='项目描述', max_length=500)
