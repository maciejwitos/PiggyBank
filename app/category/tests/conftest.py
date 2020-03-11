import os
import sys

import pytest
from django.test import Client

from app.category.tests.utils import create_fake_category
from app.models import Category

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def set_up():
    for _ in range(5):
        create_fake_category()
