"""
URL configuration for search project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from searchapp import views

# from searchapp.views import user_login,user_logout
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('searchapp/',views.searchapp, name='searchapp'),
    path('searchapp/signup/',views.register_user, name='register_user'),

    # path('signup/login.html',views.login, name='login'),

    path('searchapp/login/', views.user_login, name='user_login'),
    path('searchapp/logout/', views.user_logout, name='logout'),
    path('test-session/', views.test_session, name='test_session'),
]
