from django.urls import path
from . import views

# 어떤 주소로 들어왔을 때 어떤 View를 연결 할건지

urlpatterns = [
    path('detail/<int:pk>/', views.board_detail),
    path('list/', views.board_list),
    path('write/', views.board_write),
]
