from django import forms

from .models import Prisoner

class PrisonerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    second_name = forms.CharField(max_length=100)
    date_of_conclusion = forms.DateTimeField()
    image = forms.ImageField()

    class Meta:
        model = Prisoner
        fields = ('first_name', 'second_name', 'date_of_conclusion')