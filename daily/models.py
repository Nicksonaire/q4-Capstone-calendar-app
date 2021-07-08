from django.db import models


class Habit(models.Model):
    # trigger = models.
    action = models.TextField()
    reward = models.CharField(max_length=100)


class DailyPlan(models.Model):
    what = models.TextField()
    when = models.DateField()
    who = models.TextField()
