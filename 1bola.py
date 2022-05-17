class Bola:

  def __init__(self,cor,circunferencia,material):
    self.cor = cor
    self.circunferencia = circunferencia
    self.material = material

  def trocacor (self, cor):
    self.cor = cor

  def mostrarcor (self):
    print (f'A cor da bola é: {self.cor}')

bola1 = Bola('verde',14,'borracha')
bola1.mostrarcor ()
bola1.trocacor('amarelo')
bola1.mostrarcor ()