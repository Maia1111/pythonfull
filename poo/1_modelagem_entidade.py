
class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistma(self):
        print(f'{self.nome} esta logando no sistema.')


p1 = Pessoas(nome='Rogerio', idade=35, cpf=99999999999)


p1.logar_sistma()

