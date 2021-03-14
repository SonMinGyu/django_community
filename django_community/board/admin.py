from django.contrib import admin
from .models import Board

# Register your models here.


class BoardAdmin(admin.ModelAdmin):  # admin 페이지에서 유저에 대한 정보를 어떻게 보여줄 것인가
    list_display = ('title', 'contents', 'writer', 'registered_dttm')


admin.site.register(Board, BoardAdmin)  # 내가 만든 유저 테이블을 적용하는 코드
