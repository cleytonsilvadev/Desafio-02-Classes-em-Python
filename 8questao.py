class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f'Os pontos são: {self.x} e {self.y}')


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centro(self):
        self.altcent = self.altura / 2
        self.largcent = self.largura / 2

    def trocartamanho(self):
        self.largura = float(input('Digite a largura: '))
        self.altura = float(input('Digite a altura: '))


retangulo1 = Retangulo(10, 14)
retangulo1.centro()
meio = Ponto(retangulo1.largcent, retangulo1.altcent)
meio.imprimir()
while True:
    opcao = int(input('[1]Digitar a área \n [2]Calcular quantidade de ceramicas'))
    if (opcao == 1):
        retangulo1.trocartamanho()
    elif (opcao == 2):
        retangulo1.centro()
        meio = Ponto(retangulo1.largcent, retangulo1.altcent)
        meio.imprimir()
    else:
        break