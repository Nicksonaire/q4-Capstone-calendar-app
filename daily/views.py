from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from cal_app.models import MyUser, Goal
from .forms import DailyPlanForm
from .models import DailyPlan
from datetime import date
from django.utils.safestring import mark_safe
import re

def daily_view(request, username):
    all_goals = Goal.objects.filter(assigned_to=request.user)
    date_ = request.GET.get("day")
    day = date_[0:-1] if re.search("/", date_) else date_
    today_goals = []
    for goal in all_goals:
        if date.fromisoformat(day) >= goal.start and date.fromisoformat(day) <= goal.end:
            today_goals.append(goal)
    user = MyUser.objects.get(username=username)
    day_list = DayList(user, today_goals, day)
    day_list_html = day_list.format_goals()


    return render(request, "daily.html", {'user': user, 'day_list': mark_safe(day_list_html), "day": request.GET.get("day")})

class DayList:
    def __init__(self, user=None, goals=None, day=None):
        self.goals = goals
        self.user = user
        self.day = day

    def format_plans(self, plans):
        plan_list = ""
        for plan in plans:
            plan_list += f"<li key={plan.id}><div>What to do today:{plan.what}</div><div>When to do it by: {plan.when}</div><div>Who can help: {plan.who}</div></li>"
        return f"<ul>{plan_list}</ul>"

    def format_goals(self):
        html =""
        for goal in self.goals:
            plans = DailyPlan.objects.filter(goal=goal, day_assigned=date.fromisoformat(self.day))
            html+= f"<li key={goal.id}><h3>{goal.goal}</h3><button type='button'><a href='/user/{self.user.username}/create_plan?goal={goal.id}&day={self.day}/'>Add Plan</a></button>"
            if plans:
                html += f"{self.format_plans(plans)}</li>"
            else:
                html += "</li>"
        return f"<ul>{html}</ul>"


    # class DailyPlan(models.Model):
    # goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    # what = models.TextField()
    # when = models.TimeField()
    # day_assigned = models.DateField()
    # # who = models.TextField()


def add_daily_plan(request, username):
    if request.user.is_authenticated:
            if request.method == "POST":
                form = DailyPlanForm(request.POST)
                print(form.errors)
                if form.is_valid():
                    goal = Goal.objects.get(id=request.GET.get("goal"))
                    date_ = request.GET.get("day")
                    data = form.cleaned_data
                    day = date_[0:-1] if re.search("/", date_) else date_
                    DailyPlan.objects.create(
                        goal = goal,
                        what = data['what'],
                        who = data['who'],
                        when = data['when'],
                        day_assigned = date.fromisoformat(day)
                    )
                    return redirect(f"/user/{username}/dayview?day={request.GET.get('day')}")

            form = DailyPlanForm()
            return render(request, "generic_form.html", { 'form': form})
            