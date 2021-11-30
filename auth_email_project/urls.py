"""auth_email_project URL Configuration

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
from sqrapp.views import home, weath , addtask , showtask , search , deletetask , weath1
from auapp.views import user_signup, user_login, user_logout, user_rp, main, user_rp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",main,name="main"),
    path("user_signup",user_signup,name="user_signup"),
    path("user_login",user_login,name="user_login"),
    path("user_logout",user_logout,name="user_logout"),
    path("user_rp", user_rp, name="user_rp"),
    path("home", home, name="home"),
    path("user_rp", user_rp, name="user_rp"),
    path("weath", weath, name="weath"),
    path("weath1", weath1, name="weath1"),
    path("addtask", addtask, name="addtask"),
    path("showtask", showtask, name="showtask"),
    path("search", search , name="search"),
    path("deletetask/<id>", deletetask , name="deletetask"),             
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
