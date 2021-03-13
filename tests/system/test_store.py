from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel
import json


class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/store/test_store')

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_username('test_store'))
                self.assertDictEqual({'name': 'test', 'items': []}, json.loads(response.data))


    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test_store')

                response = client.get('store/test_store')

                self.assertEqual(response.status_code, 200)


    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('store/test_store')

                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'}, json.loads(response.data))


    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test_store')
                # or StoreModel('test_store').save_to_db()

                response = client.delete(' store/test_store')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'}, json.loads(response.data))


    def create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test_store')
                response = client.post('/store/test_store')

                self.assertEqual(response.status_code, 400)
                #self.assertDictEqual({'message': 'A store with name already exists.'}, json.loаds(response.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test_store')
                ItemModel('test_item', 19.99, 1).save_to_db()

                response = client.get('store/test_store')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'name': 'test',
                                      'items': [{'name': 'test_item', 'price': 19.99}]},
                                     json.loads(response.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test_store').save_to_db()

                response = client.get('/store')
                self.assertDictEqual({'stores': [{'name': 'test_store', 'items': []}]},
                                     json.loads(response.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                ItemModel('test_item', 19.99, 1).save_to_db()

                response = client.get('/store')
                self.assertDictEqual({'stores': [{'name': 'test_store', 'items': [{'name': 'test_item', 'price': 19.99}]}]},
                                     json.loads(response.data))


