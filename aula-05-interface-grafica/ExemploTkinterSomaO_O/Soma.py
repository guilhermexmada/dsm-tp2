from tkinter import *
 
class Soma_Numeros:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()
 
        # ATRIBUTOS PRIVADOS
        self.__n1 = 0
        self.__n2 = 0
        self.__soma = 0
 
    @property
    def _n1(self):
        return self.__n1
 
    @_n1.setter
    def _n1(self, value):
        self.__n1 = value
 
    @property
    def _n2(self):
        return self.__n2
 
    @_n2.setter
    def _n2(self, value):
        self.__n2 = value
 
    @property
    def _soma(self):
        return self.__soma
 
    @_soma.setter
    def _soma(self, value):
        self.__soma = value
 
 
    def configurar_tela(self):
        self.tela.title("Aplicacao O_O")
        self.tela.configure(background="gray")
 
        # DEFINE O TAMANHO PADRAO DA SUA TELA
        largura = 800
        altura = 300
 
        # PEGA A LARGURA E ALTURA DA TELA DO WINDOWS
        largura_screen = self.tela.winfo_screen()
        altura_screen = self.tela.winfo_screenheight()
 
        # DEFINE O POSICIONAMENTO CENTRALIZADO
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2
 
        # CONSTROI A TELA DE ACORDO COM AS DIMENSÕES DA TELA DO WINDOWS
        # %D SUBSTITUI CADA NÚMERO   % CONCATENA CADA VARIAVEL, LARGURA, ALTURA...
        self.tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
 
    def criar_componentes(self):
        # CRIAR FRAME pad x pady = espaçamento padding
        self.frame = Frame(self.tela, bg= "blue", padx= 20 , pady = 20)
        # Pack posiciona de acordo com a tela expand => ocupa espaço na tela ao redimensionar
        self.frame.pack(expand=True)

        # Titulo
        self.titulo = Label(self.frame, text="Soma de números: ")

        # Grid => cria grade, row = linha, colum = coluna, columspan = espaço interno da coluna
        # Pady = espaçamento parte de cima e de baixo de 10px
        self.titulo.grid(row=0, column= 0, columnspan= 2, pady= 10)

        # Numero 1
        # Stick = "w" posicionamento do texto lado esquerdo (oeste)
        Label(self.frame, text="Número 1: ").grid(row=1, column= 0, sticky="w", pady= 5)
        self.txt_n1 = Entry(self.frame)
        self.txt_n1.grid(row=1, column= 1, pady=5)

        # Numero 2
        Label(self.frame, text="Número 2: ").grid(row=3, column= 0, sticky="w", pady= 5)
        self.txt_n2 = Entry(self.frame)
        self.txt_n2.grid(row=3, column= 1, pady=5)

        # Resultado
        Label(self.frame, text="Resultado: ").grid(row=4, column= 0, sticky="w", pady= 5)
        self.txt_result = Entry(self.frame)
        self.txt_result.grid(row=4, column= 1, pady=5)

        # Botão
        self.btn_botao = Button(self.frame, text="Calcular", command=self.calcular)
        self.btn_botao.grid(row=5, column=0, columnspan=2, pady=15)

    def calcular(self):
        # Recebendo os valores das caixas de texto e guardando atributos
        self._n1 = float(self.txt_n1.get())
        self._n2 = float(self.txt_n2.get())
        self._soma = self._n1 + self._n2
        
        self.txt_result.insert(0, self._soma)

    def executar(self):
        self.tela.mainloop()