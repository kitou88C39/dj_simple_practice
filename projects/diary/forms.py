from django import forms
from .models import Day

class DayCreateForm(forms.ModelForm):

    class Meta:
        models=Day
        field="__all__"