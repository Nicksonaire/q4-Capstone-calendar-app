from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime
from month_app.models import Month
from month_app.utils import Calendar

# Create your views here.
class CalendarView(generic.ListView):
    model = Month
    template_name = "calendar.html"

    def get_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get("day", None))

        month_app = Calendar(d.year, d.month)
        html_month_app = month_app.month(withyear=True)
        context["calendar"] = mark_safe(html_month_app)
        return context

    def get_date(req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split("-"))
            return date(year, month, day=1)
        return datetime.today()
