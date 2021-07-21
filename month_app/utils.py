from datetime import datetime, timedelta
from calendar import HTMLCalendar
from cal_app.models import Goal, MyUser
from daily.models import DailyPlan


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, user=None):

        self.year = year
        self.month = month
        self.user = user
        super(Calendar, self).__init__()

    def formatday(self, day, goals):

        daily = goals.filter(end__day=day)
        formatted_month = str(self.month).rjust(2, '0') if len(str(self.month)) < 2 else self.month
        formatted_day = str(day).rjust(2, '0') if len(str(day)) <2 else day
        d = ""
        for goal in daily:
            d += f"<li> {goal.goal}</li>"
        if day != 0:
            return f"<td><span><a href='/user/{self.user.username}/dayview?day={self.year}-{formatted_month}-{formatted_day}'>{day}</a></span><ul> {d} </ul></td>"
        return "<td></td>"

    def formatweek(self, theweek, goals):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, goals)
        return f"<tr> {week} </tr>"

    def formatmonth(self, withyear=True):
        goals = Goal.objects.filter(
            end__year=self.year, end__month=self.month
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
