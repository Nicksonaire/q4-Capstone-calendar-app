from django.contrib import admin
from cal_app.models import MyUser, Goal
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(MyUser)
admin.site.register(MyUser, UserAdmin)
admin.site.register(Goal)
