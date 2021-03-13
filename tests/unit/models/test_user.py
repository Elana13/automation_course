from models.user import UserModel
from tests.base_test import BaseTest
from tests.unit.test_unit_base import UnitBaseTest


class UserTests(UnitBaseTest):
    def create_user(self):
        user = UserModel('Test name', 123)

        self.assertEqual('Test name', user.username)
        self.assertEqual(123, user.password)