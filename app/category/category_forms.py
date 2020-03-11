from app.forms import *


class AddCategoryForm(forms.Form):
    name = forms.CharField(max_length=16)
    spending = forms.HiddenInput()
    user = forms.HiddenInput()