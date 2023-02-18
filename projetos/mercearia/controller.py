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
            print('A categoria que deseja alater não existe')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')


x = ControllerCategoria()
x.AlterarCategoria('Laticinios', 'Frutas')
