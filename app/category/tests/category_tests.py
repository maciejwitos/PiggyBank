from django.contrib.auth.models import User
from django.http import response

from app.category.tests.conftest import *
from app.category.tests.utils import get_random_user
from app.models import Category


@pytest.mark.django_db
def test_add_new_category():
    lenght = Category.objects.count()
    create_fake_category()
    assert lenght + 1 == Category.objects.count()


@pytest.mark.django_db
def test_create_category_view():

    assert response.HttpResponse('/category/add/', {'name': 'Kategoria',
                                                    'user': get_random_user()}).status_code == 200