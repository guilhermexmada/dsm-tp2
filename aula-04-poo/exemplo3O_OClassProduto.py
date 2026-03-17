class Produto:
    def __init__(self,nome,preco,qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    # método p mostrar informações
    def mostrar(self):
        print('Nome do produto: ', self.nome)
        print('Preço do produto: ', self.preco)
        print('Quantidade do produto: ', self.qtd)

    # método p calcular valor total
    def calcularTotal(self):
        valorTotal = self.qtd * self.preco
        print('Total a pagar: ', valorTotal)

# instanciar objeto e chamar métodos
prod = Produto('abacate',4.9,76)
prod.mostrar()
prod.calcularTotal()