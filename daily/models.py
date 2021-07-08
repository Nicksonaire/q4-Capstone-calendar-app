from django.db import models


class Habit(models.Model):
    # trigger = models.
    action = models.TextField()
    reward = models.CharField(max_length=100)


class DailyPlan(models.Model):
    goal = models.ForeignKey("Goal", on_delete=models.CASCADE)
    what = models.TextField()
    when = models.DateField()
    who = models.TextField()
