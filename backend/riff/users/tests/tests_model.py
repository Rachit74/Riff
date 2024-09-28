from django.test import TestCase
from ..models import Client
from django.contrib.auth.hashers import make_password

class ClientModelTest(TestCase):
    def setUp(self) -> None:
        self.user = Client.objects.create(
            username = 'test_client',
            email = 'user@email.com',
            password = make_password('clientestpassword1'),
            artist = False
        )

    def test_client_creation(self):
        self.assertEqual(self.user.username, 'test_client')
        self.assertEqual(self.user.email, 'user@email.com')
        self.assertFalse(self.user.artist)

    def test_is_artist_method(self):
        self.assertFalse(self.user.is_artist())