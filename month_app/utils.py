from datetime import datetime, timedelta
from calendar import HTMLCalendar
from month_app.models import Month


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):

        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, goals):

        daily = goals.filter(start_time_day=day)
        d = ""
        for goal in daily:
            d += f"<li> {goal.title}</li>"

        if day != 0:
            return f"<td><span>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"

    def formatweek(self, theweek, goals):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, goals)
        return f"<tr> {week} </tr>"

    def formatmonth(self, withyear=True):
        goals = Month.objects.filter(
            start_day_year=self.year, start_day_month=self.month
        )
        month_app = (
            f"<table border='0' cellpadding='0' cellspacing='0' class='calendar'>\n"
        )
        month_app += (
            f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        )
        month_app += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            month_app += f"{self.formatweek(week, goals)}\n"
        return month_app
