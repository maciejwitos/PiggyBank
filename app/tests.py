from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.test import Client, TestCase, RequestFactory

from app.category.category_config import *
from app.category.tests.conftest import *
from app.category.tests.utils import get_random_user
from app.models import Category
from app.transactions.transactins_config import ReadTransactions, AddTransaction

