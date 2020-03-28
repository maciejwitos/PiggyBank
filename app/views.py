from app.user.user_config import *
from django.db.models import Q
from app.currency.scraper.currency_scraper import *


class Dashboard(LoginRequiredMixin, View):
    """
    Main View Dashboard. When run it's:
    - updating currencies
    - showing all sections for user: categories, currencies, transactions and accounts
    - has search for transactions
    - showing total wealth of user
    """
    login_url = '/login/'

    def get(self, request):
        GetCurrencies.scrap_currencies(current_day=date.today())
        categories = Category.objects.filter(user=request.user).order_by('-spending')
        currencies = Currency.objects.all()
        transactions = Transaction.objects.filter(
            user=request.user).filter(
            date__month=date.today().month).filter(
            date__year=date.today().year).order_by('-date')
        accounts = Account.objects.filter(user=request.user).order_by('-balance')
        budgets = Budget.objects.filter(
            user=request.user).filter(
            start_date__month=date.today().month).filter(
            start_date__year=date.today().year)
        my_wealth = 0
        for account in accounts:
            balance = account.balance
            balance_in_pln = balance * account.currency.in_pln
            my_wealth += balance_in_pln
        return render(request, 'dashboard.html', {'categories': categories,
                                                  'currencies': currencies,
                                                  'transactions': transactions,
                                                  'accounts': accounts,
                                                  'budgets': budgets,
                                                  'my_wealth': float(my_wealth)})

    def post(self, request):
        data = request.POST.get('search_transaction')
        categories = Category.objects.filter(user=request.user).order_by('-spending')
        currencies = Currency.objects.all()
        # search for transaction
        transactions = Transaction.objects.filter(user=request.user).filter(
            Q(comment__icontains=data) | Q(date__icontains=data)).order_by('-date')

        accounts = Account.objects.filter(user=request.user).order_by('-balance')
        budgets = Budget.objects.filter(
            user=request.user).filter(
            start_date__month=date.today().month).filter(
            start_date__year=date.today().year)

        my_wealth = 0
        for account in accounts:
            balance = account.balance
            balance_in_pln = balance * account.currency.in_pln
            my_wealth += balance_in_pln
        return render(request, 'dashboard.html', {'categories': categories,
                                                  'currencies': currencies,
                                                  'budgets': budgets,
                                                  'transactions': transactions,
                                                  'accounts': accounts,
                                                  'my_wealth': float(my_wealth)})


class View404(View):
    """
    View for redirection after error
    """
    def get(self, request):
        return render(request, '404.html')
