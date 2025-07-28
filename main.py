
def adicionar_contato(contatos, nome, telefone, email, favorito):
    if favorito.lower() == "s":
        novo_favorito = True
    else:
        novo_favorito = False
        
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": novo_favorito}
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
        print(f"{indice}. \nNome: {nome_contato} \nTelefone: {telefone_contato} \nE-mail: {email_contato} \nFavorito: {favorito}")

def editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email, favorito):
    if favorito.lower() == "s":
        novo_favorito = True
    else:
        novo_favorito = False

    contatos[indice]["nome"] = novo_nome
    contatos[indice]["telefone"] = novo_telefone
    contatos[indice]["email"] = novo_email
    contatos[indice]["favorito"] = novo_favorito
    print(f"Contato {novo_nome} salvo com sucesso:")
    return

def alterar_favorito(contatos, indice):
    
    if contatos[indice]["favorito"]:
        status_favorito = False
        texto_favoritos = "removido dos favoritos"
    else:
        status_favorito = True
        texto_favoritos = "adicionado aos favoritos"

    contatos[indice]["favorito"] = status_favorito

    print(f"O contato de {contatos[indice]["nome"]} foi {texto_favoritos}")
    return

def ver_contatos_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            favorito = "Sim" if contato["favorito"] else "Não"
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(50*"-")
            print(f"{indice}. \nNome: {nome_contato} \nTelefone: {telefone_contato} \nE-mail: {email_contato} \nFavorito: {favorito}")

def apagar_contato(contatos, indice):
    nome_contato = contatos[indice]["nome"]
    contatos.remove(contatos[indice])
    print(f"O contato {nome_contato} foi removido corretamente.")

contatos = []

#Tela inicial da aplicação com as opções a ser mostrada aos usuarios
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

    # Recebe a escolha do usuario e aciona a condicional 
    # que chama a função responsavel para realizar a ação de escolha do usuario

    # Chama a função de adicionar usuario
    if escolha_do_usuario == "1":
        nome = input("Digite o nome completo: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")
        favorito = input("Deseja salvar este contato como favorito? (s/n): ")
        
        if favorito.lower() == "s" or "n":
            adicionar_contato(contatos, nome, telefone, email, favorito)
        else:
            print("Escolha 's' ou 'n' para salvar ou nao este contato como favorito!")

    # Chama a função para mostrar os contatos
    elif escolha_do_usuario == "2":
        if contatos:
            ver_contatos(contatos)
        else:
            print("Você nao tem contatos salvo!")

    # Chama a função para editar um contato existente
    elif escolha_do_usuario == "3":
        if contatos:
            ver_contatos(contatos)
            try: 
                indice = int(input("Digite o número do indice do contato: ")) - 1
                novo_nome = input("Digite o novo nome: ")
                novo_telefone = input("Digite o novo telefone: ")
                novo_email = input("Digite o novo e-mail: ")
                favorito = input("Deseja salvar este contato como favorito? (s/n): ")
                
                if favorito.lower() == "s" or "n":
                    editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email, favorito)
                else:
                    print("Escolha 's' ou 'n' para salvar ou nao este contato como favorito!")
            except:
                print("Digite um numero válido.")
            finally:
                continue

    
    # Chama a função para alterar um contato existente
    elif escolha_do_usuario == "4":
        ver_contatos(contatos)
        try:    
            indice = int(input("Digite o número do indice do contato: ")) - 1
            alterar_favorito(contatos, indice)
        except:
                print("Digite um numero válido.")
        finally:
            continue


    # Chama a função que mostra os contatos favoritos
    elif escolha_do_usuario == "5":
        ver_contatos_favoritos(contatos)

    # Chama a função que apaga o contato escolhido
    elif escolha_do_usuario == "6":
        ver_contatos(contatos)
        try:    
            indice = int(input("Digite o número do indice do contato a ser apagado: ")) - 1
            apagar_contato(contatos, indice)
        except:
                print("Digite um numero válido.")
        finally:
            continue
    
    # Finaliza o while e encerra o aplicativo
    elif escolha_do_usuario == "7":
        print("\nPrograma finalizado.")
        break
    elif escolha_do_usuario:
        print("\nDigite apenas o numero da opção dejesada.")