from app.user.user_config import *

'''
NOTATKI
#KOD
- posortować views na modele i ich funkcje CRUD
- albo posortować na bazie CRUD

#WALUTY
- dodając walutę generujesz automatycznie scrappera, który idzie na stronę
  i nastawia wybraną walutę i jej wartość. 
'''

'''
Widok strony głównej
'''


def index(request):
    return render(request, "index.html")


class Dashboard(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        categories = Category.objects.filter(user=request.user).order_by('-spending')
        currencies = Currency.objects.all()
        transactions = Transaction.objects.filter(user=request.user).order_by('-date')
        accounts = Account.objects.filter(user=request.user).order_by('-balance')
        return render(request, 'dashboard.html', {'categories': categories,
                                                  'currencies': currencies,
                                                  'transactions': transactions,
                                                  'accounts': accounts})

