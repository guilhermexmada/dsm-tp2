# classe carro

class Carro:
    # construtor da classe
    def __init__(self, nome):
        self.nome = nome # atributo = parâmetro

        # método da classe carro
        def acelerar(self):
            print(self.nome, ' está acelerando...')
        
# instanciando objeto
car = Carro('Gol')
print(car.nome)
car.acelerar()

c = Carro('Uno')
print(c.nome)
c.acelerar()