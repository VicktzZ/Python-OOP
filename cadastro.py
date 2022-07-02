arr_clientes = []

def cadastrar():
    from Cliente import Cliente
    from limpar import limpar
    import time
    from main import main

    limpar()

    nome = input('Digite o nome do cliente: ')
    cpf = int(input('Digite o CPF do cliente: '))
    email = input('Digite o email do cliente: ')
    nasc = input('Digite o nascimento do cliente (DD/MM/AAAA): ')
    senha = input('Digite a senha do cliente: ')

    limpar()
    print('Cadastrando usuário...')
    time.sleep(2)

    cliente = Cliente(nome, cpf, email, nasc, senha)
    arr_clientes.append(cliente)

    limpar()
    print('Usuário cadastrado com suscesso!\n')
    print(cliente.nome)
    print(cliente.cpf)
    print(cliente.email)
    print(cliente.nasc)
    print(cliente.senha)
    time.sleep(4)

    main()