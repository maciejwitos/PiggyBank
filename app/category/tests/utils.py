import pytest
from django.contrib.auth.models import User

from app.models import Category, Account


def get_random_user():
    user = User.objects.create(username='test', password='123456789')
    return user


def create_fake_category():
    users = get_random_user()
    print(users)
    Category.objects.create(name='TestKategoria')