from app.forms import *


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('date', 'amount', 'user', 'category', 'account', 'comment', )

    def __init__(self, user, *args, **kwargs):
        super(AddTransactionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget=forms.SelectDateWidget()
        self.fields['category'].queryset = Category.objects.filter(user=user)
        self.fields['account'].queryset=Account.objects.filter(user=user)
        self.fields['user'].widget=forms.HiddenInput()