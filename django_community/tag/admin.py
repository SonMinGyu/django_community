from django.contrib import admin
from .models import Tag  # 추가

# Register your models here.


class TagAdmin(admin.ModelAdmin):  # admin 페이지에서 유저에 대한 정보를 어떻게 보여줄 것인가
    list_display = ('name', 'registered_dttm')


admin.site.register(Tag, TagAdmin)
