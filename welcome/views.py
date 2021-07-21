from django.shortcuts import render, HttpResponseRedirect, reverse
from cal_app.models import MyUser

# Create your views here.
def welcome_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(f"/user/{request.user.username}")
    return render(request, "index.html")