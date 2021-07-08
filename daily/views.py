from django.shortcuts import render

def daily_view(request):
    return render(request, "daily.html", {'user': request.user})