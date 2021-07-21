from django import http
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from user_stuff.forms import MyUserForm, LoginForm
from cal_app.models import MyUser, Goal, Dream
from cal_app.forms import GoalForm, DreamForm
from daily.models import DailyPlan
from django.utils.safestring import mark_safe
# Create your views here.

class Register_View(View):  
    template = "generic_form.html"

    def get(self, request):
        form = MyUserForm()
        return render(request, self.template, {"form": form, "register": True})

    def post(self, request):
        form = MyUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username = data["username"],
                password = data["password"],
                email = data["email"],
                age = data["age"],
                name = data["name"],
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(f"/user/{user.username}/")



class ProfileView(View):

    def get(self, request, username):
        user = MyUser.objects.get(username=username)
        dreams = Dream.objects.filter(owner=user)
        dream_list = self.List(user, dreams)
        dream_list_html = dream_list.format_dreams()
        return render(request, "profile.html", {"user": user, "dream_list": mark_safe(dream_list_html)})

    class List:
        def __init__(self, user,  dreams):
            self.dreams = dreams
            self.user = user

        def format_goals(self, goals):
            goal_list = ''
            for goal in goals:
                goal_list = f"<li key={goal.id}><h3>{goal.goal}</h3><p>from {goal.start} to {goal.end}</p>"
            return f"<ul>{goal_list}</ul>"

        def format_dreams(self):
            html = f"<h2>Dreams</h2><button type='button'><a href='/user/{self.user.username}/create_dream'>Add New Dream</a></button>"
            if self.dreams:
                dream_list = ''
                for dream in self.dreams:
                    goals = Goal.objects.filter(dream=dream)
                    dream_list += f"<li key={dream.id}><h3>{dream.dream}</h3><h2>Goals</h2><button type='button'><a href='/user/{self.user.username}/{dream.id}/create_goal'>Add New Goal</a></button>"
                    if goals:
                        dream_list += f"{self.format_goals(goals)}</li>"
                html += f"<ul>{dream_list}</ul>"
                return html



class LoginView(View):
    template = "generic_form.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template, {"form": form, "login": True})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(f"/user/{user.username}/")
            form = LoginForm()
            input_error = "username or password is invalid"
            return render(request, self.template, {"form": form, "input_error": input_error})


def signout(request, username):
    user = MyUser.objects.get(username=username)
    logout(request)
    return HttpResponseRedirect("/")
            