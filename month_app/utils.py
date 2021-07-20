from datetime import datetime, timedelta
from calendar import HTMLCalendar
from cal_app.models import Goal, MyUser
from daily.models import DailyPlan


class Calendar(HTMLCalendar):
	def __init__(self, user_id, year=None, month=None):
		self.user_id = user_id
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, goals):
		goals_per_day = goals.filter(end__day=day)
		d = ''
		for goal in goals_per_day:
			d += f'<li><a href=></a> {goal.goal} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, goals):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, goals)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		user = MyUser.objects.get(id=self.user_id)
		goals = Goal.objects.filter(assigned_to=user, end__year=self.year, end__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, goals)}\n'
		return cal
