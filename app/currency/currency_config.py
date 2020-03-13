from django.views.generic import UpdateView

from app.user.user_config import *
from app.currency.currency_form import *


class AddCurrency(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = AddCurrencyForm()
        return render(request, 'currency/currency_form.html', {"form": form})

    def post(self, request):
        form = AddCurrencyForm(request.POST)
        if form.is_valid():
            Currency.objects.create(
                name=form.cleaned_data['name'],
                in_pln=form.cleaned_data['in_pln']
            )
            return redirect('all-currency')
        return redirect('all-currency')


class ReadCurrency(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        currencies = Currency.objects.all()
        return render(request, 'currency/currency_all.html', {"currencies": currencies})


class EditCurrency(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Currency
    fields = ('name', 'in_pln')
    success_url = '/currency/all/'


class DeleteCurrency(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Currency
    success_url = reverse_lazy('/currency/all/')
