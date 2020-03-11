from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=3)
    in_pln = models.DecimalField(default=1, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=24)
    spending = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=24)
    bank = models.CharField(max_length=12)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(timezone.now())
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    comment = models.CharField(max_length=36)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.comment
