from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')

    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):  # 클레스를 문자열로 변환할 때 어떻게 변환하는지 수정하는 함수
        return self.name

    class Meta:
        db_table = 'community_tag'  # db_table 이름 설정
        verbose_name = "커뮤니티 태그"
        verbose_name_plural = "커뮤니티 태그"
