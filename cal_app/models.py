from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField(max_length=40)


class Goal(models.Model):
    dream = models.CharField(max_length=200)
    goal = models.CharField(max_length=200)
    what = models.TextField()
    when = models.DateTimeField(auto_now_add=True)
    who = models.TextField()
    assigned_by = models.ForeignKey(
        MyUser,
        related_name="assigned_by",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
