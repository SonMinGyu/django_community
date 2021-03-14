from django.urls import path
from . import views

# 어떤 주소로 들어왔을 때 어떤 View를 연결 할건지

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]
