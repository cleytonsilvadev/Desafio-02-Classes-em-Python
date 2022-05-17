
class Bichinho:
    def __init__(self, nome, fome, saude, idade, tedio, humor=''):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio
        self.humor = humor

    def alterarnome(self, nome):
        self.nome = nome

    def alimentar(self, tam):
        self.fome += tam
        if self.fome > 100:
            self.fome = 100

    def brincar(self, tempo):
        self.tedio += tempo
        if self.tedio > 100:
            self.tedio = 100

    def saude(self, saude):
        self.saude = saude

    def idade(self, idade):
        self.idade = idade

    def mostrarnome(self):
        print(f'O nome desse Tamagushi é: {self.nome}\n a sua fome é de: {self.fome}\n a sua saude é {self.saude}\n a sua idade é: {self.idade}')

    def calcularhumor(self):
        if (self.fome <= 25 and self.saude < 50):
            self.humor = 'estou triste e doente.'
        elif (self.fome <= 25 and self.saude >= 50):
            self.humor = 'estou triste mas estou saudável'
        elif (self.fome > 25 and self.saude < 50):
            self.humor = 'estou sem fome mas estou doente'
        else:
            self.humor = 'estou totalmente bem'
        print(f'Ola meu nome é: {self.nome} e {self.humor}')

    def mostrarStatus(self):
        print(f'{self.fome}% de fome {self.tedio}% de tedio {self.saude}% de saude')

Tamagushi = Bichinho('Pou', 50, 50,5, 50)
Tamagushi.calcularhumor()
Tamagushi.brincar(12)
Tamagushi.mostrarStatus()