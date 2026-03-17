class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    # método calcular idade
    def calculaIdade(self):
        anoAtual = int(input('Digite o ano atual: '))
        return anoAtual - self.idade
    
# instanciar objeto
p = Pessoa('Guilherme',19)
pe = Pessoa('Matheus',18)
# print(p.calculaIdade())
print(f'Você {p.nome} nasceu em {p.calculaIdade()}')
print(f'Você {pe.nome} nasceu em {pe.calculaIdade()}')
    