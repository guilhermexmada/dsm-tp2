# importar classe produto
from Produto import Produto

class Principal:
    # método estático : chama apenas atributos/métodos de outra classe
    @staticmethod
    def main():
        # instanciar classe produto
        prod = Produto()
        # chamar os métodos
        prod.cadastrarProduto()
        prod.mostrarProduto()
        print(f'Valor Total: R${prod.calcular()}')

# define inicialização da classe Principal
if __name__ == '__main__':
    Principal.main()