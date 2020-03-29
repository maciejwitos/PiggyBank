from app.budgets.budgets_form import *
from app.user.user_config import *


class AddBudget(View):

    def get(self, request):
        form = AddBudgetForm(request.user, initial={'user': request.user})
        return render(request, 'budget_form.html', {'form': form})

    def post(self, request):
        form = AddBudgetForm(request.user, request.POST, initial={'user': request.user})
        if form.is_valid():
            Budget.objects.create(user=request.user,
                                  category=form.cleaned_data['category'],
                                  budget=form.cleaned_data['budget'],
                                  date=form.cleaned_data['date'])
            return redirect('dashboard')
        else:
            return redirect('404')