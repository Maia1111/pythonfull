from model import Pessoa


class PessoaDal:

    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    @classmethod
    def ler(cls):
        nome = 'Caio'
        idade = 20
        cpf = '00000000000000'
        return Pessoa(nome, idade, cpf)
