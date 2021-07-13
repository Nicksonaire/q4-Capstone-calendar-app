from datetime import datetime, timedelta
from calendar import HTMLCalendar
from cal_app.models import Goal, Dream
from daily.models import DailyPlan


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, goals, dailies):
		goals_per_day = goals.filter(end__day=day)
		dailies_per_day = dailies.filter(day_assigned__day=day)
		d = ''
		for goal in goals_per_day:
			d += f'<li><a href=></a> {goal.goal} </li>'
		for daily in dailies_per_day:
			d += f'<li><a href=></a> {daily.what} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, goals, dailies):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, goals, dailies)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		goals = Goal.objects.filter(end__year=self.year, end__month=self.month)
		dailies = DailyPlan.objects.filter(day_assigned__year=self.year, day_assigned__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, goals, dailies)}\n'
		return cal
