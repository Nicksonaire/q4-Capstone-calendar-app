from cal_app.models import MyUser
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from user_stuff.forms import MyUserForm
from cal_app.models import MyUser
# Create your views here.

class Register_View(View):
    template_name = "generic_form.html"

    def get(self, request):
        form = MyUserForm()
        return render(request, self.template_name, {"form": form})

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
        special_user = MyUser.objects.get(id=user_id)
        return render(request, "profile.html", {"special_user": special_user})