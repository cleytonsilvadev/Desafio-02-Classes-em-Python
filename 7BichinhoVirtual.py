class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade, humor=''):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = humor

    def alterarnome(self, nome):
        self.nome = nome

    def fome(self, fome):
        self.fome = fome

    def saude(self, saude):
        self.saude = saude

    def idade(self, idade):
        self.idade = idade

    def mostrarnome(self):
        print(
            f'O nome desse Tamagushi é: {self.nome}\n a sua fome é de: {self.fome}\n a sua saude é {self.saude}\n a sua idade é: {self.idade}')

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


Tamagushi = Bichinho('Pou', 50, 50, 5)
Tamagushi.calcularhumor()