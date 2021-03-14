from django.db import models

# Create your models here.


class Board(models.Model):  # 유저 가입 모델
    title = models.CharField(max_length=128, verbose_name='제목')

    contents = models.TextField(verbose_name='내용')

    writer = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, verbose_name="작성자")
    # on_delete=models.CASCADE 는 작성자의 계정이 삭제되면 그 게시글도 같이 삭제하겠다는 의미

    tags = models.ManyToManyField('tag.Tag', verbose_name="태그")

    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='가입시간')

    def __str__(self):  # 클레스를 문자열로 변환할 때 어떻게 변환하는지 수정하는 함수
        return self.title

    class Meta:
        db_table = 'community_board'  # db_table 이름 설정
        verbose_name = "커뮤니티 게시글"
        verbose_name_plural = "커뮤니티 게시글"
