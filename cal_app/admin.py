from django.contrib import admin
from call_app.models import MyUser, Goal
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(MyUser, UserAdmin)
admin.site.register(Goal)
