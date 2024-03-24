# Created by @mksmvnv

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/<int:post_id>/', views.post, name='post'),
    path('posts/editor/', views.editor, name='editor'),
]
