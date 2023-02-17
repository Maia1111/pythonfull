from dal import PessoaDal
from model import Pessoa


class PessoaControler:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 2 and (int(idade) > 0 and int(idade) < 200) and len(cpf) == 11:
            try:
                PessoaDal.salvar(Pessoa(nome, idade, cpf))
                return True
            except:
                return False
        else:
            return False


PessoaControler.cadastrar('Jose', 20, '99999999999')
