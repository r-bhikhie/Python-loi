class Car:
    nr_wheels = 4
    def __init__(self, logo):
         self.logo = logo
    def honk(self):
         print('Honkhonk!')
    def start(self):
         print('Firing up...')

class Morse(Car):
    nr_wheels = 3
    def honk(self):
        print('Beep!')

auto1 = Car('OEMlogo')
morse1 = Morse('duck')
