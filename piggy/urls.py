from django.contrib import admin
from django.urls import path, include

from app.accounts.accounts_config import *
from app.category.category_config import *
from app.currency.currency_config import *
from app.budgets.budgets_config import *
from app.transactions.transactins_config import *
from app.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('', Dashboard.as_view()),
    path('404/', View404.as_view(), name='404'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', SignUp.as_view(), name='register-form'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user/password_change.html',
                                                                   success_url='/password_change/done/'),
         name='change-password'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_success.html'),
         name='change-password-success'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password-reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),
    path('details/', UserDetails.as_view(), name='user-details'),

    path('category/add/', AddCategory.as_view(), name='add-category'),
    path('category/all/', ReadCategories.as_view(), name='all-category'),
    path('category/details/<pk>/', DetailsCategory.as_view(), name='category-details'),
    path('category/edit/<pk>/', EditCategory.as_view(template_name='category/category_edit.html'),
         name='edit-category'),
    path('category/delete/<pk>/',
         DeleteCategory.as_view(template_name='confirm_delete.html', success_url='/category/all/'),
         name='delete-category'),

    path('account/add/', AddAccount.as_view(), name='add-account'),
    path('account/all/', ReadAccounts.as_view(), name='all-account'),
    path('account/details/<pk>/', DetailsAccount.as_view(), name='account-details'),
    path('account/edit/<pk>/', EditAccount.as_view(template_name='account/account_edit.html'), name='account-edit'),
    path('account/delete/<pk>/',
         DeleteAccount.as_view(template_name='confirm_delete.html', success_url='/account/all/'),
         name='delete-account'),

    path('transaction/add/', AddTransaction.as_view(), name='add-transaction'),
    path('transaction/all/', ReadTransactions.as_view(), name='all-transaction'),
    path('transaction/edit/<pk>/', EditTransaction.as_view(template_name='transaction/transaction_edit.html'),
         name='transaction-edit'),
    path('transaction/delete/<pk>/',
         DeleteTransaction.as_view(template_name='confirm_delete.html', success_url='/transaction/all'),
         name='delete-transaction'),

    path('currency/add/', AddCurrency.as_view(), name='add-currency'),
    path('currency/all/', ReadCurrency.as_view(), name='all-currency'),
    path('currency/edit/<pk>/', EditCurrency.as_view(template_name='currency/currency_edit.html'),
         name='edit-currency'),
    path('currency/delete/<pk>/',
         DeleteCurrency.as_view(template_name='confirm_delete.html', success_url='/currency/all'),
         name='delete-currency'),

    path('budget/add/', AddBudget.as_view(), name='add-budget'),
    path('budget/all/', ViewBudgets.as_view(), name='all-budget'),
    path('budget/delete/<pk>/', DeleteBudget.as_view(template_name='confirm_delete.html', success_url='/budget/all/'),
         name='delete-budget'),
    path('budget/edit/<pk>/', EditBudget.as_view(template_name='budget/budget_edit.html'), name='account-edit'),

]
