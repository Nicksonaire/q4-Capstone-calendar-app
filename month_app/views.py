from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime, date
from month_app.utils import Calendar
from cal_app.models import Goal

# Create your views here.

class CalendarView(generic.ListView):
    model = Goal
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            d = self.get_date(self.request.GET.get("day", None))

            month_app = Calendar(self.request.user.id, d.year, d.month)
            html_month_app = month_app.formatmonth(withyear=True)
            context["calendar"] = mark_safe(html_month_app)
            return context

    def get_date(self, req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split("-"))
            return date(year, month, day=1)
        return datetime.today()
# from django.shortcuts import render, get_object_or_404

# # from django.http import HttpResponse, HttpResponseRedirect
# from django.views.generic import DetailView, RedirectView
# from month_app.models import Event

# # from django.urls import reverse
# # from django.utils.safestring import mark_safe
# import datetime


# # from .models import Month

# # from month_app.utils import HTMLCalendar
# # import calendar
# # from calendar import HTMLCalendar
# from django.shortcuts import render
# from django.contrib import messages
# from month_app.bcal import get_bcal


# def calendar(request, year, month, day):
#     today = datetime.datetime.now()
#     today_events = (
#         Event.objects.filter(date__year=year)
#         .filter(date__month=month)
#         .filter(date__day=day)
#     )
#     if int(month) > 12:
#         y = str(today.year)
#         m = str(today.month)
#         messages.add_message(request, messages.WARNING, "Month error")
#     else:
#         y = year
#         m = month

#     return render(
#         request,
#         "month_app.html",
#         {
#             "calendar": get_bcal(y, m, day),
#             "today": today_events,
#         },
#         # content_type="html",
#     )


# class CalendarRedirect(RedirectView):
#     permanent = False
#     today = datetime.datetime.now()
#     url = "/month_app/calendar/%i/%i/%i" % (today.year, today.month, today.day)


# class EventList(DetailView):
#     model = Event
#     template_name = "event_detail.html"
