from django.shortcuts import render
from cal_app.models import MyUser, Goal
from .forms import DailyPlanForm
from .models import DailyPlan
from datetime import date

def daily_view(request, username):
    all_goals = Goal.objects.filter(assigned_by=request.user)
    today_goals = []
    for goal in all_goals:
        if date.today() > goal.start and date.today < goal.end:
            today_goals.append(goal)
            
    user = username if request.user.is_authenticated else "None"
    return render(request, "daily.html", {'user': user, 'goals': today_goals})


def add_daily_plan(request, username):
    if request.user.is_authenticated:
            if request.method == "POST":
                form = DailyPlanForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    DailyPlan.objects.create(
                        goal = data['goal'],
                        what = data['what'],
                        who = data['who'],
                        when = data['when'],
                        day_assigned = data['day_assigned']
                    )

            form = DailyPlanForm()
            return render(request, "generic_form.html", { 'form': form})
            