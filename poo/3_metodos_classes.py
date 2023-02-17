class Pessoas():
    possui_olho = True
    possui_boca = True
    raca = 'Ser humano'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def andar(cls):
        cls.pernas = 2
        return None


p1 = Pessoas('Marcos', 22)
p2 = Pessoas('José', 34)


print(Pessoas.andar())

print(Pessoas.pernas)


@staticmethod
def adulto(idade):
    if idade > 18:
        return True
    return False

# Utilizando atributo static


print(adulto(21))
