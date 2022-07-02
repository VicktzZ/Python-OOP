def listar():
    from cadastro import arr_clientes
    from limpar import limpar
    from main import main
    import time

    limpar()

    for i in range(len(arr_clientes)):
        print(f'| NOME: {arr_clientes[i].nome}      | CPF: {arr_clientes[i].cpf}     | EMAIL: {arr_clientes[i].email}     | NASC: {arr_clientes[i].nasc}     | SENHA: {arr_clientes[i].senha} |     ')
        print("\n\n")
    
    input('Aperte enter para continuar...')
    main()
