class Cliente:
    _contadorId = 0

    def  __init__(self, nome:str, telefone:str, email:str, cpf:str):
        Cliente._contadorId += 1
        self.id = Cliente._contadorId
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf

class Quartos:
    def __init__(self, numeroQuarto:int, tipoDeQuartos:int, precoDaDiaria:float, statusDeDisponibilidade:int):
        self.numeroQuarto = numeroQuarto
        self.tipoDeQuarto = tipoDeQuartos
        self.precoDaDiaria = precoDaDiaria
        self.statusDeDisponibilidade = statusDeDisponibilidade

class Reserva:
    def __init__(self, donoDaReserva:int, quartoReservado:int, dataCheckin:str, dataCheckout:str, statusDaReserva:bool):
        self.donoDaReserva = donoDaReserva
        self.quartoReservado = quartoReservado
        self.dataCheckin = dataCheckin
        self.dataCheckout = dataCheckout
        self.statusDaReserva = statusDaReserva

class Hotel:
    def __init__(self):
        self.listaDeClientes = []
        self.listaDeQuartos = []
        self.listaDeReservas = []

    def adicionarCliente(self):
        nome = input("Digite o Nome do Cliente: ")
        telefone = input("Digite o Telefone do Cliente: ")
        email = input("Digite o Email do Cliente: ")
        cpf = input("Digite o CPF do Cliente: ")
        cliente = Cliente(nome, telefone, email, cpf)
        self.listaDeClientes.append(cliente)
        print(f"Cliente {cliente.nome} Cadastrado com sucesso")

    def verTodosCliente(self):
        if not self.listaDeClientes:
            print("Nenhum cliente foi encontrado...")
            return
        
        for cliente in self.listaDeClientes:
            print(f"""
    ID: {cliente.id}
    Nome: {cliente.nome}
    Telefone: {cliente.telefone}
    Email : {cliente.email}

""")

    def modificarCliente(self):
        identifier = int(input("Digite o ID do Cliente que Deseja Modificar: "))
        for cliente in self.listaDeClientes:
            if cliente.id == identifier:
                modificar = input("""
O que você deseja modificar:
1 - Nome do Cliente
2 - Telefone do Cliente
3 - Email do Cliente
0 - Não Desejo Modificar Nada
""")
                match modificar:
                    case "1":
                        nome = input("Digite o Novo Nome do Cliente: ")
                        cliente.nome = nome
                    case "2":
                        telefone = input("Digite o Novo Telefone do Cliente: ")
                        cliente.telefone = telefone
                    case "3":
                        email = input("Digite o Novo Email do Cliente: ")
                        cliente.email = email
                    case "0":
                        print("Voltando para o Menu Clientes")
                        pass
                    case _:
                        pass

    def excluirCliente(self):
        identifier = int(input("Digite o ID do Cliente que Deseja Exluir: "))
        for cliente in self.listaDeClientes:
            if cliente.id == identifier:
                self.listaDeClientes.remove(cliente)
                print(f"{cliente.nome} foi excluído com sucesso")
                return
        print("Cliente Não Encontrado...")


    def adicionarQuarto(self):
        tipo = ["Single", "Double", "Suite"]
        disponibilidade = [True, False] #True = Disponivel e False = Indisponivel
        numeroQuarto = int(input("Digite o Número do Quarto: "))
        while True:
            tipoQuarto = int(input(f"""Digite o tipo do Quarto:
    === Tipos de Quarto ===
1 - Single
2 - Double
3 - Suite
"""))
            if tipoQuarto in [1, 2, 3]:
                tipoQuarto = tipo[tipoQuarto - 1]
                break
            else:
                print("Opção Inválida. Tente Novamente\n")
            
        print(f"O Tipo de Quarto Escolhido Foi: {tipoQuarto}")

        precoDiaria = float(input("Digite o Preço da Diária do Quarto: R$"))
        while True:
            statusDisponibilidade = int(input("""Digite a Disponibilidade do Quarto:
=== Disponibilidade do Quarto ===
1 - Disponível
2 - Indisponível
"""""))
            if statusDisponibilidade in [1, 2]:
                statusDisponibilidade = disponibilidade[statusDisponibilidade - 1]

                if statusDisponibilidade == True:
                    statusDisponibilidade = "Disponível"
                elif statusDisponibilidade == False: 
                    statusDisponibilidade = "Indisponível"
                break
            else:
                print("Opção Inválida. Tente Novamente...")
        print(f"O Quarto Está {statusDisponibilidade}")

        quarto = Quartos(numeroQuarto, tipoQuarto, precoDiaria, statusDisponibilidade)
        self.listaDeQuartos.append(quarto)
        print(f"O Quarto {quarto.numeroQuarto} Foi Cadastrado com sucesso")

    def verTodosQuarto(self):
        if not self.listaDeQuartos:
            print("Nenhum quarto foi encontrado...")
            return
        
        for quarto in self.listaDeQuartos:
            print(f"""
    Número: {quarto.numeroQuarto}
    Tipo: {quarto.tipoDeQuarto}
    Preço (Diária): R${quarto.precoDaDiaria:.2f}
    Disponibilidade : {quarto.statusDeDisponibilidade}

""")

    def verQuartosDisponiveis(self):
        if not self.listaDeQuartos:
            print("Nenhum quarto foi encontrado...")
            return
        
        for quarto in self.listaDeQuartos:
            if quarto.statusDeDisponibilidade == "Disponível":
                print(f"""
    Número: {quarto.numeroQuarto}
    Tipo: {quarto.tipoDeQuarto}
    Preço (Diária): R${quarto.precoDaDiaria:.2f}
    Disponibilidade : {quarto.statusDeDisponibilidade}

""")


    def modificarQuarto(self):
        tipo = ["Single", "Double", "Suite"]
        disponibilidade = ["Disponível", "Indisponível"]
        numeroQuarto = int(input("Digite o Número do Quarto que Deseja Modificar: "))

        encontrado = False
        
        for quarto in self.listaDeQuartos:
            if quarto.numeroQuarto == numeroQuarto:
                encontrado = True
                print(f"Quarto selecionado: {quarto.numeroQuarto}")
                modificar = input("""
O que você deseja modificar:
1 - Número do Quarto
2 - Tipo do Quarto
3 - Preço da Diária do Quarto
4 - Status de Disponibilidade do Quarto
0 - Não Desejo Modificar Nada
""")
                match modificar:
                    case "1":
                        novoNumero = int(input("Digite o Novo Número do Quarto: "))
                        if novoNumero != quarto.numeroQuarto:
                            if any(q.numeroQuarto == novoNumero for q in self.listaDeQuartos):
                                print("Esse número de quarto já existe. Escolha outro.")
                            else:
                                quarto.numeroQuarto = novoNumero
                                print("Número do quarto atualizado com sucesso!")
                        else:
                            print("O número do quarto permanece o mesmo.")

                    case "2":
                        while True:
                            tipoQuarto = int(input("""Digite o tipo do Quarto:
    === Tipos de Quarto ===
1 - Single
2 - Double
3 - Suite
"""))
                            if tipoQuarto in [1, 2, 3]:
                                quarto.tipoDeQuarto = tipo[tipoQuarto - 1]
                                print(f"O Tipo de Quarto foi atualizado para: {quarto.tipoDeQuarto}")
                                break
                            else:
                                print("Opção Inválida. Tente Novamente.")

                    case "3":
                        precoDiaria = float(input("Digite o Novo Preço da Diária do Quarto: "))
                        quarto.precoDaDiaria = precoDiaria
                        print(f"Preço da Diária atualizado: R${quarto.precoDaDiaria:.2f}")

                    case "4":
                        while True:
                            novaDisponibilidade = int(input("""Novo Status de Disponibilidade:
1 - Disponível
2 - Indisponível
"""))
                            if novaDisponibilidade in [1, 2]:
                                if quarto.statusDeDisponibilidade != disponibilidade[novaDisponibilidade - 1]:
                                    quarto.statusDeDisponibilidade = disponibilidade[novaDisponibilidade - 1]
                                    print(f"Nova disponibilidade: {quarto.statusDeDisponibilidade}")
                                else:
                                    print("O Quarto já possui esse status.")
                                break
                            else:
                                print("Opção inválida. Tente novamente.")

                    case "0":
                        print("Voltando para o Menu Quartos...")
                    
                    case _:
                        print("Opção inválida. Tente novamente.")

                break

        if not encontrado:
            print("O Quarto digitado não existe. Tente novamente...")


    def excluirQuarto(self):
        numeroQuarto = int(input("Digite o Número do Quarto que Deseja Excluir: "))
        for quarto in self.listaDeQuartos:
            if quarto.numeroQuarto == numeroQuarto:
                self.listaDeQuartos.remove(quarto)
                print(f"O Quarto {quarto.numeroQuarto} foi excluído com sucesso")
                return
        print("Quarto Selecionado Não Encontrado...")

    
    def adicionarReserva(self):
        pass

    def verTodosReserva(self):
        pass

    def modificarReserva(self):
        pass

    def excluirReserva(self):
        pass