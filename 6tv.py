class Tv:
    def __init__(self, numerocanal, volume):
        self.numerocanal = numerocanal
        self.volume = volume

    def trocarcanal(self, canal):
        self.numerocanal = canal
        if (self.numerocanal > 20):
            self.numerocanal = 20
        print(f'O canal atual é: {self.numerocanal}')

    def aumentarvolume(self):
        if (self.volume < 100):
            self.volume += 1
        print(f'O volume agora é: {self.volume}')

    def baixarvolume(self):
        if (self.volume > 0):
            self.volume -= 1
        print(f'O volume agora é: {self.volume}')


tv = Tv(8, 14)
tv.trocarcanal(150)
tv.aumentarvolume()
tv.baixarvolume()