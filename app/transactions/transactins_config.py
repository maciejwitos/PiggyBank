from django.views.generic import UpdateView

from app.transactions.transaction_form import AddTransactionForm
from app.user.user_config import *


# Dodawanie transakcji
class AddTransaction(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = AddTransactionForm(request.user, initial={'user': request.user})
        return render(request, 'transaction/transaction_form.html', {'form': form})

    def post(self, request):
        form = AddTransactionForm(request.user, request.POST, initial={'user': request.user})
        if form.is_valid():
            Transaction.objects.create(
                date=form.cleaned_data['date'],
                amount=form.cleaned_data['amount'],
                comment=form.cleaned_data['comment'],
                category=form.cleaned_data['category'],
                account=form.cleaned_data['account'],
                user=request.user
            )

            category = form.cleaned_data['category']
            category.spending += form.cleaned_data['amount']
            category.save()
            bank = form.cleaned_data['account']
            bank.balance -= form.cleaned_data['amount']
            bank.save()


            return redirect('/transaction/all/')
        return redirect('/transaction/add/')


# Wypisanie wszystkich transakcji
class ReadTransactions(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user.pk).order_by('-date')
        return render(request, 'transaction/transaction_all.html', {'transactions': transactions})


class EditTransaction(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Transaction
    fields = ('date', 'amount', 'category', 'account', 'comment')
    success_url = '/transaction/all/'


# Usuwanie transakcji
class DeleteTransaction(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Transaction
    success_url = reverse_lazy('/transaction/all/')

    def __init__(self, *args, **kwargs):
        super(DeleteTransaction, self).__init__(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # get data about deleted objects and related models
        transaction = Transaction.objects.get(id=kwargs['pk'])
        bank_balance = transaction.account
        category_spending = transaction.category
        # delete object
        result = super().delete(request, *args, **kwargs)
        # refund for category and account balance
        bank_balance.balance += transaction.amount
        category_spending.spending -= transaction.amount
        bank_balance.save()
        category_spending.save()

        return result




