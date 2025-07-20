


contatos = []
while True:
    print(50*"-")
    print("Bem vindo a sua agenda.")
    print(50*"-")

    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contatos")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Ver contatos favoritos")
    print("6. Apagar contatos")
    print("7. Sair")

    escolha_do_usuario = input("\nSelecione uma das opções para prosseguir:")

    if escolha_do_usuario == "1":
        print("Contato Adicionado")
    elif escolha_do_usuario == "7":
        print("\nPrograma finalizado.")
        break
    else:
        print("\nDigite apenas o numero da opção dejesada.")