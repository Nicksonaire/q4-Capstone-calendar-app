from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    name = models.CharField(max_length=40)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.name


class Dream(models.Model):
    dream = models.CharField(max_length=200)
    goals = models.ForeignKey("Goal", related_name="dream", on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(
        MyUser,
        related_name="%(class)s_assigned_by",
        on_delete=models.CASCADE,
    )


class Goal(models.Model):
    goal = models.CharField(max_length=200)
    start= models.DateField()
    end = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(
        MyUser,
        related_name="%(class)s_assigned_by",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )