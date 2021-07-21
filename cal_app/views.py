from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import MyUser, Goal, Dream
from .forms import GoalForm, DreamForm


@login_required(login_url="/login")
def create_goal( request, username):
            if request.method == "POST":
                form = GoalForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    user = MyUser.objects.get(username=username)
                    dream = Dream.objects.get(id=request.GET.get("dream"))
                    new_goal = Goal.objects.create(
                        dream = dream,
                        goal = data['goal'],
                        start = data['start'],
                        end = data['end'],
                        assigned_to = user
                    )
                    return HttpResponseRedirect(f"/user/{user.username}/")

            form = GoalForm()
            return render(request, "generic_form.html", {'form': form})


@login_required(login_url="/login")       
def create_dream( request, username):
        if request.method == "POST":
            form = DreamForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = MyUser.objects.get(username=username)
                Dream.objects.create(dream=data['dream'], owner = user)
                return HttpResponseRedirect(f"/user/{user.username}/")

        form = DreamForm()
        return render(request, "generic_form.html", {'form': form})