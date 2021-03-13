from models.store import StoreModel
from tests.unit.test_unit_base import UnitBaseTest


class StoreTest(UnitBaseTest):
    def create_store(self):
        store = StoreModel('Amazon')
        self.assertEquel('Amazon', store.name)
