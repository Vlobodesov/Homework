import random
class Animal():
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, _cords, speed):
      self._cords = _cords[0,0,0]
      self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = self._cords[0]*self.speed
        self.dy = self._cords[1] * self.speed
        self.dz = self._cords[2] * self.speed
        if self._cords[2] < 0:
            print('it is too deep, i can not dive')

    def get_cords(self):
        return f'X:{self.dx}, Y: {self.dy}, Z: {self.dz}'

    def attack(self):
        if _DEGREE_OF_DANGER < 5:
            print('Sorry, i am peaceful')
        elif _DEGREE_OF_DANGER >= 5:
            print('Be careful, i am attacking you 0_0')

    def speak(self):
        return f'sound'


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        return f'Here are(is) {random.randint(1,4)} eggs for you'

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    # def dive_in(self,dz):
    #     ????


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = 'Click-click-click'



db = Duckbill(10)



print(db.live)

print(db.beak)



db.speak()

db.attack()



db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()



db.lay_eggs()
