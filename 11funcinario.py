class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def verSalario(self):
        print(f'Ola {self.nome} seu salário é de R${self.salario}')

pessoa = Funcionario('Bartolomeu', 2677.78)
pessoa.verSalario()