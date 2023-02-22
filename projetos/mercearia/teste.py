from datetime import datetime

from dao import *
from models import *


class ControllerVenda:

    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):

        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if isinstance(i.quantidade, str):
                        try:
                            i.quantidade = int(
                                ''.join(filter(str.isdigit, i.quantidade)))
                        except ValueError:
                            print('Erro ao converter quantidade para inteiro')
                            return None

                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - \
                            int(quantidadeVendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco,
                                        i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * \
                            int(i.produto.preco)

                        DaoVenda.salvar(vendido)

            # adiciona as informações atualizadas à lista temporária
            temp.append([Produtos(i.produto.nome, i.produto.preco,
                        i.produto.categoria), i.quantidade])

        if existe == False:
            print('Produto não existe!')
            return None
        elif not quantidade:
            print('O estoque é insuficiente para a quantidade vendida!')
        else:
            # escreve as informações atualizadas no arquivo
            with open('venda.txt', 'a') as arq:
                arq.writelines(vendido.produto.nome + "|" + vendedor + "|" +
                               comprador + "|" + str(quantidadeVendida) + "|" + str(valorCompra))
                arq.writelines('\n')

            print('Venda Realizada com Sucesso!')
            return valorCompra


a = ControllerVenda()
a.cadastrarVenda('banana', 'Jose', 'Marcos', 2)
