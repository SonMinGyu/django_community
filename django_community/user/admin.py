from django.contrib import admin
from .models import User  # 추가

# Register your models here.

# 관리자에 쓸 정보


class UserAdmin(admin.ModelAdmin):  # admin 페이지에서 유저에 대한 정보를 어떻게 보여줄 것인가
    list_display = ('username', 'password', 'userEmail', 'registered_dttm')


admin.site.register(User, UserAdmin)  # 내가 만든 유저 테이블을 적용하는 코드
