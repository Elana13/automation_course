from models.user import UserModel
import json

from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username': 'test', 'password': 'pass123'})

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully'}, json.loаds(response.data))


    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username': 'test', 'password': 'pass123'})

                auth_response = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': 'pass123'}),
                                           headers={'Content-Type': 'application/json'})
                self.assertIn('access_token', json.loads(auth_response.data).keys())


    def test_register_thesame_user(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username': 'test', 'password': 'pass123'})
                response = client.post('/register', data={'username': 'test', 'password': 'pass123'})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': 'A user with username already exists'}, json.loаds(response.data))
