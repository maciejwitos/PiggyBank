from app.user.user_config import *
from app.accounts.accounts_forms import *


# Dodawanie nowego konta
class AddAccount(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = AddAccountForm()
        return render(request, 'account/account_form.html', {'form': form})

    def post(self, request):
        form = AddAccountForm(request.POST)
        if form.is_valid():
            Account.objects.create(
                name=form.cleaned_data['name'],
                bank=form.cleaned_data['bank'],
                currency=form.cleaned_data['currency'],
                balance=form.cleaned_data['balance'],
                user=request.user
            )
            return redirect('all-account')
        return redirect('all-account')

# Wyświetlanie wszystkich kont
class ReadAccounts(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        accounts = Account.objects.filter(user=request.user.pk)
        return render(request, 'account/account_all.html', {'accounts': accounts})


# Wyświetlanie jednego konta
class ReadOneAccount(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        account = Account.objects.get(id=id)
        return render(request, 'account/account_details.html', {'account': account})


# Usuwanie konta
class DeleteAccount(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Account
    success_url = reverse_lazy('/account/all/')
