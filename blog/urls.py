from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


"""
slug -> это тоже самое что charfild, но для урлов(ссылок)
"""
# cache_page это 15 минут, это для хеширования запросиков
urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', views.PostListView.as_view(), name="post_list"),
    # Если раскомментить запросы будут ждать 15 минут и фотки будут стягиваться 15 минут
    # path('', cache_page(60 * 15)(views.HomeView.as_view()), name="home"),
    path('', views.HomeView.as_view(), name="home"),
]