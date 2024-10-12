from abc import ABC, abstractmethod
from datetime import date

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(f"Depósito de {self.valor} realizado.")
            return True
        return False

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if 0 < self.valor <= conta.saldo:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque de {self.valor} realizado.")
            return True
        return False

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            sucesso = transacao.registrar(conta)
            if sucesso:
                print(f"Transação realizada: {transacao.__class__.__name__} de {transacao.valor}")
            else:
                print("Transação falhou.")
        else:
            print("Conta não pertence ao cliente.")

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
        cliente.adicionar_conta(self)

    def sacar(self, valor):
        saque = Saque(valor)
        return saque.registrar(self)

    def depositar(self, valor):
        deposito = Deposito(valor)
        return deposito.registrar(self)

    @staticmethod
    def nova_conta(cliente, numero, agencia):
        return Conta(numero, agencia, cliente)

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = 0

    def sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            self.limite_saques += 1
            return super().sacar(valor)
        return False

cliente = PessoaFisica("123.456.789-00", "João Silva", date(1990, 5, 20), "Rua A, 123")
conta = ContaCorrente(1, "0001", cliente, 500)

cliente.realizar_transacao(conta, Deposito(200))
cliente.realizar_transacao(conta, Saque(100))
