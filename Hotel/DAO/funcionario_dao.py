from Hotel.DAO.dao import Dao
from Hotel.model.funcionario import Funcionario
class FuncionarioDao(Dao):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario: Funcionario):
        if (isinstance(funcionario, Funcionario)):
            super().add(funcionario.cracha, funcionario)

    def get(self, key):
        super().get(key)

    def remove(self, key):
        super().remove(key)

