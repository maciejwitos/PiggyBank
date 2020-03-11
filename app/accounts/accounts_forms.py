
from app.forms import *


class AddAccountForm(forms.Form):
    name = forms.CharField(max_length=16)
    bank = forms.CharField(max_length=16)
    balance = forms.FloatField()
    user = forms.HiddenInput()
    currency = forms.ModelChoiceField(queryset=Currency.objects.all())
