from django.urls import path
from . import views


"""
slug -> это тоже самое что charfild, но для урлов(ссылок)
"""
urlpatterns = [
    path('<slug:slug>', views.PostListView.as_view(), name="post_list"),
    path('', views.home),
]