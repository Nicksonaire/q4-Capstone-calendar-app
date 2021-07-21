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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from user_stuff import views as user_views
from cal_app import views as main_views
from daily import views as daily_views
from welcome.views import welcome_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_view, name="index"),
    path("register/", user_views.Register_View.as_view()),
    path("user/<username>/", login_required(
        user_views.ProfileView.as_view(), login_url="/login"),
        name="user-main"),
    path("user/<username>/dayview/", daily_views.daily_view, name="dayview"),
    path("user/<username>/create_dream/", main_views.create_dream),
    path("user/<username>/create_goal/", main_views.create_goal),
    path("user/<username>/create_plan/", daily_views.add_daily_plan),
    path("user/<username>/", include("month_app.urls")),
    path("user/<username>/logout/", user_views.signout),
    path("login/", user_views.LoginView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
