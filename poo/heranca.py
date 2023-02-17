class Pessoa():

    def falar(self):
        print('Estou falando')

    def andar(self):
        print('estou andando')


class Cliente(Pessoa):

    def comprar(self):
        print('Estou comprando')


class Vendedor(Pessoa):

    def vender(self):
        print('Estou vendendo')


c1 = Cliente()

c1.andar()
c1.falar()


v1 = Vendedor()

v1.vender()

