"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import splash, login_view, signup_view, logout_view, delete, profile_view, home_view, hashtag_view, like, delete_home, like_home, hashtag_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name='splash'),
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('delete', delete, name='delete'),
    path('delete_home', delete_home, name='delete_home'),
    path('profile/<str:username>', profile_view, name='profile'),
    path('home', home_view, name='home'),
    path('hashtag/<str:hashtag>', hashtag_view, name='hashtag'),
    path('hashtag', hashtag_home, name='hashtag'),
    path('like_home', like_home, name='like_home'),
    path('like', like, name='like')
]
