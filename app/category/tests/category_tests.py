from app.tests import *

@pytest.mark.django_db
def test_add_new_category():
    lenght = Category.objects.count()
    create_fake_category()
    assert lenght + 1 == Category.objects.count()


class UrlTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@user.com', password='top_secret')

    def test_category_add_url(self):
        request = self.factory.post('/category/add/')
        request.user = self.user
        response = AddCategory.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_category_all_url(self):
        request = self.factory.get('/category/all/')
        request.user = self.user
        response = ReadCategories.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_category_delete_url(self):
        Category.objects.create(name='Kate', user=self.user)
        request = self.factory.get('/category/delete/1')
        request.user = self.user
        response = DeleteCategory.as_view()(request)
        self.assertEqual(response.status_code, 200)
