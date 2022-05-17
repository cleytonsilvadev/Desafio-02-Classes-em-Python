import random


class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if (self.idade < 21):
            self.altura += 0.5

    def engordar(self):
        self.peso += random.randint(1, 5)

    def emagrecer(self):
        self.peso -= random.randint(1, 3)

    def crescer(self):
        self.altura += random.random()

    def mostrardados(self):
        print(
            f'A idade de {self.nome} é {self.idade} anos, o seu peso é de {self.peso}Kg, sua altura é de {self.altura:.2f}M')


Cleyton = Pessoa('cleyton', 26, 40, 1.70)
Cleyton.mostrardados()
Cleyton.envelhecer()
Cleyton.mostrardados()
Cleyton.engordar()
Cleyton.mostrardados()
Cleyton.emagrecer()
Cleyton.mostrardados()
Cleyton.crescer()
Cleyton.mostrardados()