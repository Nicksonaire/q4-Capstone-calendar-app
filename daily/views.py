from django.shortcuts import render
from cal_app.models import MyUser

def daily_view(request, username):
    user = username if request.user.is_authenticated else "Not Logged In"
    return render(request, "daily.html", {'user': user})


def add_daily_plan(request, username):
    if request.user.is_authenticated:
        if request.user.username == username:
            user = MyUser.objects.get(username=username)
            