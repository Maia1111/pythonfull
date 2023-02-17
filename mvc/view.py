from controller import PessoaControler

while True:
    opcao = int(input(
        'Digite 1 para salvar uma pessoa ou digite 2 para ver a pessoa salva e 3 sair: '))
    if opcao == 3:
        break
    if opcao == 1:
        nome = input('Digite o nome da pessoa: ')
        idade = input('Digite a idade da pessoa: ')
        cpf = input('Digite o cpf da pessoa: ')
        if PessoaControler.cadastrar(nome, idade, cpf):
            print('Usuário cadastrado com sucesso!')
        else:
            print('Digite valores válidos!')
