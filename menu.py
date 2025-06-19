from contato import Contato
import banco

def exibir_menu():
    while True:
        print("\n--- Menu de Contatos --- ")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Atualizar Contatos")
        print("4. Remover Contatos")
        print("5. Sair")


        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            contato = Contato(nome, telefone, email)
            banco.adicionar_contato(contato) 

        elif opcao == "2":
            contatos = banco.listar_contatos()
            if not contatos:
                print("Nenhum contato encontrado.")
            else:
                for c in contatos: print(f"ID: {c[0]} | Nome: {c[1]} | Telefone: {c[2]} | Email: {c[3]}")

        elif opcao == "3":
            try: 
                id = int(input("Digite o ID do contato a atualizar: "))
                nome = input("Novo nome: ")
                telefone = input("Novo telefone: ")
                email = input("Novo email: ")
                contato = Contato(nome, telefone, email)
                banco.atualizar_contato(id, contato)

            except ValueError:
                print("ID inválido")

        elif opcao == "4":
            try:
                id = int(input("Digite o ID do contato a remover: "))
                banco.remover_contato(id)
            except ValueError:
                print("ID inválido")
        
        elif opcao == "5":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválido por favor tente novamente.")




         
