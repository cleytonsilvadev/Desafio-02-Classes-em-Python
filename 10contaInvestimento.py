class contaInvestimento:
    def __init__(self, numeroconta, nometitular, taxaJuros, saldo=0):
        self.numeroconta = numeroconta
        self.nometitular = nometitular
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def alterarnome(self, nome):
        self.nometitular = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicioneJuros(self, juros=10):
        self.saldo *= (juros/100)+1

    def mostrarsaldo(self):
        print(f'Bom dia {self.nometitular} o seu saldo é de: {(self.saldo):.2f}')

pessoa = Conta(1324131, 'Carl', 10, 1000.00)
for c in range(5):
    pessoa.adicioneJuros()
pessoa.mostrarsaldo()