# Run this with python -i to land in the interactive shell.

class Person:
    pop = 0
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
        Person.pop += 1
        self.paperclips = 0
    def __del__(self):
        Persoon -= 1
    def __str__(self):
        # iets
        returnstring = "This is a Person object: {0} was born in {1}".format(self.name, self.yob)
        return returnstring
    def __add__(self, other):
        self.paperclips += int(other)
        print("{0} now has {1} paperclips!".format(self.name, self.paperclips))

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

alice = Person('Alice', 1996)
bob = Person('Bob', 1985)
eve = Person('Eve', 2000)

