class Pessoas():
    possui_olho = True
    possui_boca = True

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoas('Rogério', 21)
p2 = Pessoas("Marcos", 22)

print(p1.nome)
print(p2.nome)

# Acessando atributos de instancia sem instanciar um objeto
print(Pessoas.possui_olho)
