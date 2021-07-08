"""hardgoals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from user_stuff import views as user_views
from daily import views as daily_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", user_views.Register_View.as_view()),
    path("user/<user_id>/", user_views.ProfileView.as_view()),
    path("login/", user_views.LoginView.as_view()),
    path("user/<username>/daily/", daily_views.daily_view, name='daily')
]
