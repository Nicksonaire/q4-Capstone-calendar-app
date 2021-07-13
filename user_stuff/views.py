from cal_app.models import MyUser
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from user_stuff.forms import MyUserForm, LoginForm
from cal_app.models import MyUser, Goal
# Create your views here.

class Register_View(View):
    template = "generic_form.html"

    def get(self, request):
        form = MyUserForm()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = MyUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create_user(
                username = data["username"],
                password = data["password"],
                email = data["email"],
                age = data["age"],
                name = data["name"],
            )
            return HttpResponseRedirect("/")


class ProfileView(View):

    def get(self, request, user_id):
        special_user = MyUser.objects.get(username=user_id)
        goals = Goal.objects.all()
        goals = Goal.objects.filter(assigned_by=special_user)
        return render(request, "profile.html", {"special_user": special_user, "goals": goals})


class LoginView(View):
    template = "generic_form.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request, user)
                return HttpResponseRedirect("/")

def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)
def error_500(request):
        return render(request,'500.html')
