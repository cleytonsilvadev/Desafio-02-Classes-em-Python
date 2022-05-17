class ContaCorrente:
    def __init__(self, numeroconta, nometitular, saldo=0):
        self.numeroconta = numeroconta
        self.nometitular = nometitular
        self.saldo = saldo

    def alterarnome(self, nome):
        self.nometitular = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def mostrarsaldo(self):
        print(f'Bom dia {self.nometitular} o seu saldo é de: {self.saldo}')


pessoa = Conta(565656, 'Lucas', 4000)
pessoa.deposito(345.45)
pessoa.mostrarsaldo()
pessoa.saque(286)
pessoa.mostrarsaldo()