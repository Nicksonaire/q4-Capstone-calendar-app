from django.urls import path
from month_app import views


urlpatterns = [
    # path("index/", views.index_view, name="index"),
    path("calendar/", views.CalendarView.as_view(), name="calendar"),
]
