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
    owner = models.ForeignKey(
        MyUser,
        related_name="%(class)s_assigned_by",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.dream


class Goal(models.Model):
    dream = models.ForeignKey(Dream, related_name="goals", on_delete=models.CASCADE, null=True, blank=True)
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