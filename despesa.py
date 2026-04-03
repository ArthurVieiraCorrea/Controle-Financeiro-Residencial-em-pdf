from datetime import datetime

class Despesa:
    def __init__(self, valor, categoria, data, descricao):
        self.valor = float(valor)
        self.categoria = categoria
        self.data = data
        self.descricao = descricao

    def to_dict(self):
        return self.__dict__