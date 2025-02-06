from classes import *
import os # colocar no programa ou não, ainda vou ver
import time

def limpar_terminal(tempo=2):
    time.sleep(tempo)
    os.system("cls" if os.name == "nt" else "clear")




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
    os.system("cls" if os.name == "nt" else "clear")
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
                os.system("cls" if os.name == "nt" else "clear")
                match menuClientes:
                    case "1":
                        hotel.adicionarCliente()
                        limpar_terminal(tempo=0)
                    case "2":
                        hotel.verTodosCliente()
                    case "3":
                        hotel.modificarCliente()
                        limpar_terminal(tempo=0)
                    case "4":
                        hotel.excluirCliente()
                        limpar_terminal(tempo=1)
                    case "0":
                        print("Voltando ao Menu Principal...")
                        limpar_terminal(tempo=0.5)
                        break
                    case _:
                        print("Opção Inválida. Tente Novamente...")
                        limpar_terminal(tempo=0.5)

        case "2":
            while True:
                menuQuartos = input("""
        ==== Menu Quartos ===
    Digite a Opção que Deseja:
    1 - Cadastrar Novo Quarto
    2 - Ver Todos os Quartos
    3 - Verificar Quartos Disponíveis
    4 - Modificar Cadastro de Quarto
    5 - Excluir Quarto
    0 - Sair
        """)
                match menuQuartos:
                    case "1":
                        hotel.adicionarQuarto()
                        limpar_terminal(tempo=0)
                    case "2":
                        hotel.verTodosQuarto()
                    case "3":
                        hotel.verQuartosDisponiveis()
                    case "4":
                        hotel.modificarQuarto()
                        limpar_terminal(tempo=0)
                    case "5":
                        hotel.excluirQuarto()
                        limpar_terminal(tempo=1)
                    case "0":
                        print("Voltando ao Menu Principal...")
                        break
                    case _:
                        print("Opção Inválida. Tente Novamente...")
        case "3":
            print("opção 3")
        case "0":
            print("Saindo do Programa...")
            break
        case _:
            print("Opção inválida")