class Produto:
    def __init__(self):
        self.__nome = '' # __atributo : private
        self.__valor = 0
        self.__qtd = 0
    # getter nome
    def get_Nome(self):
        return self.__nome
    # setter nome
    def set_Nome(self, nome):
        self.__nome = nome
    # getter valor
    def get_Valor(self):
        return self.__valor
    # setter valor
    def set_Valor(self, valor):
        self.__valor = valor
    # getter quantidade
    def get_Qtd(self):
        return self.__qtd
    # setter quantidade
    def set_Qtd(self, qtd):
        self.__qtd = qtd
    
    # método cadastrar
    def cadastrarProduto(self):
        print('\n === Cadastro de Produtos === \n')
        self.set_Nome(input('Nome do produto: '))
        self.set_Qtd(int(input('Quantidade do produto: ')))
        self.set_Valor(float(input('Valor do produto: ')))
    # método mostrar
    def mostrarProduto(self):
        print('\n === Dados do Produto === \n')
        print('Nome: ', self.get_Nome)
        print('Quantidade: ', self.get_Qtd)
        print('Valor: ', self.get_Valor)
    # método calcular valor total
    def calcular(self):
        return self.__qtd * self.__valor