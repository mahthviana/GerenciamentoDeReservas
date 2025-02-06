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
    def __init__(self, numeroQuarto:int, tipoDeQuartos:int, PrecoDaDiaria:float, statusDeDisponibilidade:bool):
        self.numeroQuarto = numeroQuarto
        self.tipoDeQuarto = tipoDeQuartos
        self.precoDaDiaria = PrecoDaDiaria
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
        identifier = int(input("Digite o ID do Cliente que Deseja Modificar: "))
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

        precoDiaria = float(input("Digite o Preço da Diária do Quarto: "))
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
    Preço (Diária): {quarto.precoDaDiaria}
    Disponibilidade : {quarto.statusDeDisponibilidade}

""")

    def verQuartosDisponiveis(self):
        pass

    def modificarQuarto(self):
        pass

    def excluirQuarto(self):
        pass

    
    def adicionarReserva(self):
        pass

    def verTodosReserva(self):
        pass

    def modificarReserva(self):
        pass

    def excluirReserva(self):
        pass