
from django.contrib import admin
from django.urls import path,include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('posts/', views.PostListView, name='all_posts'),
    path('post/',views.Blog, name='blog')

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)