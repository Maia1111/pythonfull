from datetime import datetime

from dao import *
from models import *


class ControllerCategoria:

    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()

        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print(f'{novaCategoria} foi salvo com sucesso!')

        else:
            print('A categoria que  deseja cadastrar já existe.')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A categoria que esta tentando deletar não existe!')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def AlterarCategoria(self, cateriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == cateriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))

            if len(cat1) == 0:

                x = list(map(lambda x: Categoria(categoriaAlterada)
                         if (x.categoria == cateriaAlterar) else (x), x))
                print('Categoria Alterada com sucesso!')

            else:
                "A categoria que deseja alterar já existe"

        else:
            print('A categoria que deseja alterar não existe')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self,):
        categorias = DaoCategoria.ler()

        if len(categorias) == 0:
            print('A lista de Categorias esta vazia')

        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')


class ControllerEstoque:

    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda y: y.categoria == categoria, y))

        est = est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('Produto já existe no estoque!')
        else:
            print('Categoria inexistente!')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()

        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    print('Produto removido com sucesso!')
                    break
        else:
            print('O produto que deseja remover não existe')

        with open('estoque.txt', 'w') as arq:

            for i in x:
                arq.writelines(i.produto.nome +
                               "|" + i.produto.preco +
                               "|" + i.produto.categoria +
                               "|" + str(i.quantidade))
                arq.writelines('\n')

    def alterarEstoque(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):

        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))

        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))

            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))

                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if (
                        x.produto.nome == nomeAlterar) else (x), x))
                    print('Produto alterado com sucesso!')
                else:
                    print('Produto já cadastrado')

            else:
                print('O produto que deseja alterar não existe')
        else:
            print('A categoria informada não existe!')

        with open('estoque.txt', 'w') as arq:

            for i in x:
                arq.writelines(i.produto.nome +
                               "|" + i.produto.preco +
                               "|" + i.produto.categoria +
                               "|" + str(i.quantidade))
                arq.writelines('\n')


e = ControllerEstoque()


e.alterarEstoque('melancia', 'banana', '10', 'Frutas', 10)
