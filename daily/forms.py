from django import forms
from datetime import date
# from cal_app.models import Goal


class DailyPlanForm(forms.Form):
    # goal = forms.ChoiceField(choices=Goal.objects.all())
    what = forms.CharField()
    when = forms.TimeField()
    who = forms.CharField()
    date_assigned = forms.DateField()