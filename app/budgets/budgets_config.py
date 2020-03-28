from app.budgets.budgets_form import *
from app.user.user_config import *


class AddBudget(View):

    def get(self, request):
        form = AddBudgetForm()
        return render(request, 'budget_form.html', {'form': form})

    def post(self, request):
        form = AddBudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return redirect('404')