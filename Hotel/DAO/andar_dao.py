from DAO.dao import Dao
from model.andar import Andar

class AndarDao(Dao):
    def __init__(self):
        super().__init__('andares.pkl')

    def add(self, andar: Andar):
        if isinstance(andar, Andar):
            super().add(andar.numero, andar)

    def get(self, key):
        super().get(key)

    def remove(self, key):
        super().remove(key)