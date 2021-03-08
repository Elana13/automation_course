from tests.base_test import BaseTest

from models.store import StoreModel


class StoreTest(BaseTest):
    def create_store(self):
        store = StoreModel('Amazon')
        self.assertEquel('Amazon', store.name)
