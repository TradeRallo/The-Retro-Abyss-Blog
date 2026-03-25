from django.urls import path
from . import views


urlpatterns = [
    path('', views.news, name='news'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]

