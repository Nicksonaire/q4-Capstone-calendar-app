from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import MyUser, Goal, Dream
from .forms import GoalForm, DreamForm


# # Create your views here.
# def index_view(request):
#     return HttpResponse("connected")
@login_required(login_url="/login")
def general_view(request, username):
        dreams = Dream.objects.filter(owner=request.user)


@login_required(login_url="/login")
def create_goal(request, username):
        if request.method == "POST":
            form = GoalForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Goal.objects.create(
                    goal = data['goal'],
                    what = data['what'],
                    who = data['who'],
                    when = data['when'],
                    day_assigned = data['day_assigned']
                )

        form = GoalForm()
        return render(request, "generic_form.html", {'form': form})


@login_required(login_url="/login")
def create_dream(request, username):
        if request.method == "POST":
            form = DreamForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Dream.objects.create(dream=data['dream'])

        form = DreamForm()
        return render(request, "generic_form.html", {'form': form})
