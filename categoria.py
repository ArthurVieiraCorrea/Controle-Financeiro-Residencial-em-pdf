class Categoria:
    def __init__(self, nome, limite=0.0):
        self.nome = nome
        self.limite = limite
        self.despesas = []

    def adicionar_despesa(self, despesa):
        self.despesas.append(despesa)
        if self.limite > 0 and self.total_gasto() > self.limite:
            print(f"⚠️ ALERTA: limite de R${self.limite:.2f} excedido em '{self.nome}'!")
    
    def total_gasto(self):
        return sum(d.valor for d in self.despesas)