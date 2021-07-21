from django.db import models
from cal_app.models import Goal


class Habit(models.Model):
    # trigger = models.
    action = models.TextField()
    reward = models.CharField(max_length=100)


class DailyPlan(models.Model):
    goal = models.ForeignKey(Goal, related_name="plans", on_delete=models.CASCADE)
    what = models.TextField()
    when = models.TimeField()
    day_assigned = models.DateField()
    who = models.TextField()
