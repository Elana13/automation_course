from tests.unit.unit_base_test import BaseTest
from models.user import UserModel


class UserTests(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('Test name', 123)

            self.assertIsNone(UserModel.find_by_username('Test name'))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('Test name'))
            self.assertIsNotNone(UserModel.find_by_id(1))