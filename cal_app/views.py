from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .models import MyUser, Goal, Dream
from .forms import GoalForm


# # Create your views here.
# def index_view(request):
#     return HttpResponse("connected")

def general_view(request, username):
    if request.user.is_authenticated():
        dreams = Dream.objects.filter()


def create_goal(request, username):
    if request.user.is_authenticated:
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