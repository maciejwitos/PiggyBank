from app.forms import *


class AddBudgetForm(forms.ModelForm):

    class Meta:

        model = Budget
        fields = "__all__"
