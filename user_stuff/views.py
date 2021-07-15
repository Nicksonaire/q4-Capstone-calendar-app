from cal_app.models import MyUser
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from user_stuff.forms import MyUserForm, LoginForm
from cal_app.models import MyUser, Goal, Dream
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
                return HttpResponseRedirect(f"/user/{user.username}/daily/")



class ProfileView(View):
    template = "profile.html"

    def get(self, request, username):
        user = MyUser.objects.get(username=username)
        dreams = Dream.objects.filter(owner=user)
        return render(request, self.template, {"user": user, "dreams": dreams})


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
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(f"/user/{user.username}/daily/")
            form = LoginForm()
            input_error = "username or password is invalid"
            return render(request, self.template, {"form": form, "input_error": input_error})
            