from django.db import models
from django.contrib.auth.models import AbstractUser

def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    #아이디 비밀번호는 기존 username/password 필드 사용
    name = models.CharField(max_length=20)
    is_participant = models.BooleanField(default=False)
    #참여자 정보
    univ = models.CharField(max_length= 20, null=True, blank=True)
    team = models.IntegerField(null=True, blank=True)
    techrole = models.CharField(max_length=20, null=True, blank=True)
    #마이페이지에서 추후 프로필 사진 등록
    profile_pic = models.ImageField(upload_to=image_upload_path, null=True, blank=True) 




