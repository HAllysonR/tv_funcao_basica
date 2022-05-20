class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        self.volume = 0

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

    def aumentar_volume(self):
        if self.ligada:
            self.volume += 3

    def diminuir_volume(self):
        if self.ligada:
            self.volume -= 1

tv = Televisao()
tv.power()
print('Aumenta canal {}'.format(tv.canal))
tv.aumenta_canal()
tv.aumenta_canal()
print('Aumenta canal {}'.format(tv.canal))
tv.diminui_canal()
print('Aumenta canal {}'.format(tv.canal))

print('volume atual da tv: {}'.format(tv.volume))
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print('volume atual da tv: {}'.format(tv.volume))
