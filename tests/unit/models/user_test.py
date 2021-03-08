from tests.unit.unit_base_test import BaseTest
from models.user import UserModel


class UserTests(BaseTest):
    def create_user(self):
        user = UserModel('Test name', 123)

        self.assertEqual('Test name', user.username)
        self.assertEqual(123, user.password)