from app.tests import *

class UrlTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@user.com', password='top_secret')

    def test_transaction_all_url(self):
        # Create an instance of a GET request.
        request = self.factory.get('/transactions/all/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        # request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        # response = ReadTransactions(request)
        # Use this syntax for class-based views.
        response = ReadTransactions.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_transaction_add_url(self):
        request = self.factory.get('/transaction/add/')
        request.user = self.user
        response = AddTransaction.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_transaction_delete_url(self):
        currency = Currency.objects.create(name='PLN',
                                          in_pln=1)
        category = Category.objects.create(name='Kate', user=self.user)
        account = Account.objects.create(name='fake_bank_name',
                               bank='fake_bank',
                               balance=100,
                               currency=currency)
        transaction = Transaction.objects.create(date='2020-03-03',
                                   user=self.user,
                                   account=account,
                                   category=category,
                                   comment='fake_comment')
        request = self.factory.get(f'/transaction/delete/{transaction.pk}/')
        request.user = self.user
        response = DeleteCategory.as_view()(request)
        self.assertEqual(response.status_code, 200)