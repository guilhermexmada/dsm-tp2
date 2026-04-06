from Soma import Soma_Numeros

class Principal:
    @staticmethod
    def main():
        # Instanciar classe Soma
        som = Soma_Numeros()
        som.executar()

if __name__ == "__main__":
    Principal.main()