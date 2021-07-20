from django.urls import path
from month_app import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path("index/", views.index_view, name="index"),
    path("calendar/", login_required(
        views.CalendarView.as_view(),
        login_url="/login"
        ),
        name="calendar"),
]
