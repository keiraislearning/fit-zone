from django.forms import ModelForm
from main.models import Fit

class FitForm(ModelForm):
    class Meta:
        model = Fit
        fields = ['name', 'price', 'description', 'thumbnail', 'category']
