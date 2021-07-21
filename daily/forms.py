from django.forms import ModelForm, DateInput,TimeInput
from datetime import date
from .models import DailyPlan


class DailyPlanForm(ModelForm):
    class Meta:
        model = DailyPlan
        widgets = {
            "when" : TimeInput(attrs={'type': 'time'}, format='T%H:%M')
        }
        fields = ["what", 'when', 'who']
    
    def __init__(self, *args, **kwargs):
        super(DailyPlanForm, self).__init__(*args, **kwargs)
        self.fields["when"].input_formats = ('T%H:%M',)