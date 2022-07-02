def main():
    import time
    from limpar import limpar
    from cadastro import cadastrar
    from lista import listar

    limpar()
    print('+----------------------+')
    print('| Cadastro de clientes |')
    print('+----------------------+')
    print('1 - Para cadastrar')
    print('2 - Para listar')
    print('3 - Sair')
    
    entrada = input("\nDigite sua escolha: ") 

    if entrada == '1':
        cadastrar()
    elif entrada == '2':
        listar()
    elif entrada == '3':
        limpar()
        print('Saindo...')
        time.sleep(2)
    else:
        limpar()
        print("\nDIGITE UM NÚMERO VÁLIDO! ")
        time.sleep(1)
        main()

main()