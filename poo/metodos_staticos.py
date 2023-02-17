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

    @staticmethod
    def adulto(idade):
        if idade > 18:
            return True
        return False


print(Pessoas.adulto(21))
