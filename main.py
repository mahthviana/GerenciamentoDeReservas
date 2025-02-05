from classes import *
import os # colocar no programa ou não, ainda ou ver


hotel = Hotel()

while True:
    menu = input("""
    ==== Menu Principal ===
Digite a Opção que Deseja:
1 - Gerenciar Clientes
2 - Gerenciar Quartos
3 - Gerenciar Reservas
0 - Sair
    """)

    match menu:
        case "1":
            while True:
                menuClientes = input("""
    ==== Menu Clientes ====
1 - Cadastrar Novo Cliente
2 - Ver Todos os Clientes
3 - Modificar Cadastro de Cliente
4 - Excluir Cliente
0 - Sair
    """)

                match menuClientes:
                    case "1":
                        hotel.adicionarCliente()
                    case "2":
                        hotel.verTodosCliente()
                    case "3":
                        hotel.modificarCliente()
                    case "4":
                        hotel.excluirCliente()
                    case "0":
                        print("Voltando ao Menu Principal...")
                        break
                    case _:
                        print("Opção Inválida Tente Novamente")

        case "2":
            print("opção 2")
        case "3":
            print("opção 3")
        case "0":
            print("Saindo do Programa...")
            break
        case _:
            print("Opção inválida")
