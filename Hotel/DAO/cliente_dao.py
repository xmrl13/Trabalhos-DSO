from DAO.dao import Dao
from model.cliente import Cliente

class ClienteDao(Dao):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            super().add(cliente.cpf, cliente)

    def get(self, key):
        super().get(key)

    def remove(self, key):
        super().remove(key)
