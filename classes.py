class Cliente:
    _contadorId = 0

    def  __init__(self, nome:str, telefone:str, email:str):
        Cliente._contadorId += 1
        self.id = Cliente._contadorId
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Quartos:
    def __init__(self, numeroQuarto:int, tipoDeQuartos:str, PrecoDaDiaria:float, statusDeDisponibilidade:bool):
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
        cliente = Cliente(nome, telefone, email)
        self.listaDeClientes.append(cliente)
        print(f"Cliente {cliente.nome} Cadastrado com sucesso")

    def verTodosCliente(self):
        pass

    def modificarCliente(self):
        pass

    def excluirCliente(self):
        pass


    def adicionarQuarto(self):
        pass

    def verTodosQuarto(self):
        pass

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

