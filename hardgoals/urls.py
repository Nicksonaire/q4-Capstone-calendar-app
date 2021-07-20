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
<<<<<<< HEAD
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from user_stuff import views as user_views
from cal_app import views as main_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", user_views.Register_View.as_view()),
    path("user/<username>/", login_required(
        user_views.ProfileView.as_view(), login_url="/login"),
        name="user-main"),
    path("user/<username>/create_dream/", main_views.create_dream),
    path("user/<username>/<dream_id>/create_goal/", main_views.create_goal),
    path("user/<username>/", include("month_app.urls")),
    path("user/<username>/logout/", user_views.signout),
    path("login/", user_views.LoginView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
from django.urls import path

# from django.conf.urls.static import static
# from django.conf import settings
from month_app import views

# from rest_framework import routers

# from month_app.urls import urlpatterns as _urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.CalendarRedirect.as_view()),
    path("month_app/<pk>/", views.EventList.as_view()),
    path("month_app/calendar/<year>/<month>/<day>/", views.calendar),
    # path("", include("month_app.urls")),
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns = month_app_urls
>>>>>>> 540943b1c1b5614d2936b24239865a96261e9922
