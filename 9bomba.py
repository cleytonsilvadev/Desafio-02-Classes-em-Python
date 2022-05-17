class Bomba:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        self.litros = 0
        self.pagar = 0

    def abastecerPorValor(self, valor):
        self.litros = valor / self.valorLitro
        self.quantidadeCombustivel -= self.litros
        print(f'Foi abastecido um total de {self.litros} litros')

    def abastecerPorLitro(self, litro):
        self.pagar = litro * self.valorLitro
        self.quantidadeCombustivel -= litro
        print(f'Foi abastecido um total de {litro} litros e o valor pago será de R${self.pagar}')

    def alterarValor(self, valor):
        self.valorLitro = valor

    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo

    def alterarQuantidadeCombustivel(self, alterado):
        self.quantidadeCombustivel = alterado


carro = Bomba('Gasolina', 4, 5000)
carro.abastecerPorLitro(10)
carro.abastecerPorValor(40)