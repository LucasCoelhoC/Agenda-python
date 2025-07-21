
def adicionar_contato(contatos, nome, telefone, email, favorito):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    contatos.append(contato)
    print(f"O Contato de {nome} foi salvo com sucesso!")
    return

def ver_contatos(contatos):
    print("Lista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "Sim" if contato["favorito"] else "Não"
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(50*"-")
        print(f"{indice}. \nNome: {nome_contato} \nTelefone: {telefone_contato} \nEmail: {email_contato} \nFavorito: {favorito}")

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
        nome = input("Digite o nome completo: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        favorito = input("Deseja salvar este contato como favorito? (s/n): ")
        
        if favorito == "s" or "S":
            adicionar_contato(contatos, nome, telefone, email, favorito=True)
        elif favorito == "n" or "N":
            adicionar_contato(contatos, nome, telefone, email, favorito=False)
        else:
            print("Escolha 's' ou 'n' para salvar ou nao este contato como favorito!")

    elif escolha_do_usuario == "2":
        if contatos:
            ver_contatos(contatos)
        else:
            print("Você nao tem contatos salvo!")

    elif escolha_do_usuario == "7":
        print("\nPrograma finalizado.")
        break
    elif escolha_do_usuario:
        print("\nDigite apenas o numero da opção dejesada.")