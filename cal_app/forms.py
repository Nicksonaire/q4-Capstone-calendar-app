from django import forms
from .models import Dream


class GoalForm(forms.Form):
    dream = forms.ChoiceField()
    goal = forms.CharField(max_length=200)
    start = forms.DateField()
    end = forms.DateField()


class DreamForm(forms.Form):
    dream = forms.CharField(max_length=200)