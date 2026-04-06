from tkinter import *
# Criando Tela do Tkinter - Interface Gráfica
tela = Tk()

# Título
tela.title("Fatec Registro")

# Cor de fundo
tela.configure(background="#1259b0")
# Tamanho da tela
tela.geometry("700x500")

# Redimensionar tela true = habilita / false = desabilita
tela.resizable(True, False)
# Define o tamanho máximo para redimensionar
tela.minsize(width=400, height= 600)
# Define o tamanho mínimo para redimensionar
tela.maxsize(width=700, height=800)

# Criando Label
lbl_nome = Label(tela, text="Digite o seu nome: ", background="#1259b0", foreground="#ffffff", font="Aria 15 bold italic").place(x=10,y=60)
lbl_tel = Label(tela, text="Digite o seu número: ", bg= "#1259b0", fg="#ffffff", font=("Aria", "15", "bold", "italic")).place(x=10,y=130)

# Criando caixa de texto

txt_nome = Entry(tela, width=50, borderwidth=3, background="#000000", fg="white")
txt_nome.place(x=10,y=90)
txt_numero = Entry(tela, width=50, borderwidth=3, background="#000000", fg="white")
txt_numero.place(x=10,y=160)

# Criando método para o botão
def mostradados():
    lbl_mostra = Label(tela, text="Bem-vindo " + txt_nome.get() + "! \n telefone: " + txt_numero.get())
    lbl_mostra.place(x=10, y= 265)

# Criando botão
btn_botão = Button(tela, text="Mostrar Dados", command=mostradados)
btn_botão.place(x=10, y=220)

# Executando Tela
tela.mainloop()