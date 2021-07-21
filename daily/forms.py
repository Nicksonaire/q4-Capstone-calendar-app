from django.forms import ModelForm, DateInput,TimeInput
from datetime import date
from .models import DailyPlan


class DailyPlanForm(ModelForm):
    class Meta:
        model = DailyPlan
        widgets = {
            "when" : TimeInput(attrs={'type': 'time'})
        }
        fields = ["what", 'when', 'who']