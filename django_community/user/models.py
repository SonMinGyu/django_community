from django.db import models

# Create your models here.


class User(models.Model):  # 유저 가입 모델
    username = models.CharField(max_length=32, verbose_name='사용자명')

    userEmail = models.EmailField(max_length=128, verbose_name='사용자이메일')

    password = models.CharField(max_length=64, verbose_name='비밀번호')

    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='가입시간')

    def __str__(self):  # 클레스를 문자열로 변환할 때 어떻게 변환하는지 수정하는 함수
        return self.username

    class Meta:
        db_table = 'community_user'  # db_table 이름 설정
        verbose_name = "커뮤니티 사용자"
        verbose_name_plural = "커뮤니티 사용자"
