from DAO.dao import Dao
from model.quarto import Quarto

class QuartoDao(Dao):
    def __init__(self):
        super().__init__('quartos.pkl')

    def add(self, quarto: Quarto):
        if isinstance(quarto, Quarto):
            super().add(quarto.numero_do_quarto, quarto)

    def get(self, key):
        super().get(key)

    def remove(self, key):
        super().remove(key)