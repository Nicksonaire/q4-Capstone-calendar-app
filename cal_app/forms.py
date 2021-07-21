from django.forms import Form, ModelForm, DateInput
from django import forms
from .models import Dream, Goal


class GoalForm(ModelForm):
    class Meta:
        model = Goal
        widgets = {
            'start': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'end': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            }
        fields = ["goal", "start", "end"]

    def __init__(self, *args, **kwargs):
        super(GoalForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start'].input_formats = ('%Y-%m-%d',)
        self.fields['end'].input_formats = ('%Y-%m-%d',)


class DreamForm(Form):
    dream = forms.CharField(max_length=200)