from app.user.user_config import *
from app.category.category_forms import *


class AddCategory(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = AddCategoryForm()
        return render(request, 'category/category_form.html', {'form': form})

    def post(self, request):
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(
                name=form.cleaned_data['name'],
                spending=0,
                user=request.user
            )
            return redirect('all-category')
        return redirect('all-category')


# Wyświetlanie wszystkich kategorii
class ReadCategories(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        categories = Category.objects.filter(user=request.user.pk)
        return render(request, 'category/category_all.html', {'categories': categories})


# Usuwanie kategorii
class DeleteCategory(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Category
    success_url = reverse_lazy('/category/all/')