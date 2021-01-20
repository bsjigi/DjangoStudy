from django.urls import path
from . import views

# urlpatterns는 path() 함수의 리턴값들로 이루어진 리스트여야 한다
urlpatterns = [
    path('', views.main),
    path('news/', views.news_main),
    path('news/article1', views.article1),
    path('news/article2', views.article2),
]
