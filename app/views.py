from app.user.user_config import *
from django.db.models import Q
from django.core.paginator import Paginator


class Dashboard(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        categories = Category.objects.filter(user=request.user).order_by('-spending')
        categories_paginator = Paginator(categories, 6)
        page_number = request.GET.get('page')
        page_objects = categories_paginator.get_page(page_number)
        currencies = Currency.objects.all()
        transactions = Transaction.objects.filter(user=request.user).order_by('-date')
        accounts = Account.objects.filter(user=request.user).order_by('-balance')
        my_wealth = 0
        for account in accounts:
            balance = account.balance
            balance_in_pln = balance * account.currency.in_pln
            my_wealth += balance_in_pln
        return render(request, 'dashboard.html', {'categories': categories ,
                                                  'currencies': currencies,
                                                  'transactions': transactions,
                                                  'accounts': accounts,
                                                  'my_wealth': float(my_wealth)})

    def post(self, request):
        data = request.POST.get('search_transaction')
        categories = Category.objects.filter(user=request.user).order_by('-spending')
        currencies = Currency.objects.all()
        transactions = Transaction.objects.filter(user=request.user).filter(
            Q(comment__icontains=data) | Q(date__icontains=data)).order_by('-date')

        accounts = Account.objects.filter(user=request.user).order_by('-balance')
        my_wealth = 0
        for account in accounts:
            balance = account.balance
            balance_in_pln = balance * account.currency.in_pln
            my_wealth += balance_in_pln
        return render(request, 'dashboard.html', {'categories': categories,
                                                  'currencies': currencies,
                                                  'transactions': transactions,
                                                  'accounts': accounts,
                                                  'my_wealth': float(my_wealth)})


class View404(View):

    def get(self, request):
        return render(request, '404.html')
