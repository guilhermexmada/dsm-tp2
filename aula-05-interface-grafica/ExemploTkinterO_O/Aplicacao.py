from tkinter import *

class Aplicacao:
    def __init__(self):
        self.tela = Tk()
        self.configurarTela()
        self.criarComponentes()

    def configurarTela(self):
        self.tela.title("Aplicação O_O")
        self.tela.configure(background="#3f90c2")

        # Define o tamanho padrão da sua tela
        largura = 800
        altura = 300

        # Pega a largura e altura da tela do windows
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        # Define o posicionamento centralizado
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        # Constroi a tela de acordo com as dimensões da tela do windows
        # %d substitui cada número       % concatena com as variaveis
        self.tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

    def criarComponentes(self):
        self.txtnome = Entry(self.tela , width = 20, borderwidth=3)
        self.txtnome.pack()

    def executar(self):
        self.tela.mainloop()