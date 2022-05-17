class Retangulo:

    def __init__(self, tamanhoA, tamanhoB):
        self.tamanhoA = tamanhoA
        self.tamanhoB = tamanhoB

    def trocartamanho(self, tamanhoA, tamanhoB):
        self.tamanhoA = tamanhoA
        self.tamanhoB = tamanhoB

    def retornartamanho(self):
        print(f'O tamanho do lado A do retangulo é: {self.tamanhoA} e o lado B é: {self.tamanhoB}')

    def calculoarea(self):
        print(
            f'O tamanho da area do retangulo é: {self.tamanhoA * self.tamanhoB} e o seu perimentro é: {2 * (self.tamanhoA * self.tamanhoB)}')


retangulo1 = Retangulo(6, 12)

opcao = int(input('[1]Digitar a área \n [2]Calcular quantidade de ceramicas'))
if (opcao == 1):
    tamanhoA = float(input('Digite a base: '))
    tamanhoB = float(input('Digite a altura: '))
    retangulo1.trocartamanho(tamanhoA, tamanhoB)
elif (opcao == 2):
    retangulo1.calculoarea()
    area = (retangulo1.tamanhoA * retangulo1.tamanhoB) * 1000
    print(
        f'Para ceramicas 20x30 a quantidade utilizada será de {area / 600} unidades, para ceramicas 40x40 a quantidade utilizada será de {area / 1600} unidades e para ceramicas 60x60 a quantidade utilizada será de {area / 3600} unidades')
