class Animal:
    voice = ''
    ration = ''

    def make_voice(self):
        print(self.voice)
    
    
class Bird(Animal):
    ration = 'Зерно'
    fly = None


class Mammals(Animal):
    ration = 'Трава'


class Cow(Mammals):
    voice = 'Му'

    #  r-рацион,c-количество травы. Возвращает n - литров молока по формуле n=c/2
    def get_milk(self, r, c):
        if r == self.ration:
            return c/2
        else:
            return 'Я не ем ' + r


class Sheep(Mammals):
    voice = 'Бееее'
    max_wool = 5

    def get_wool(self, c):
        if c <= self.max_wool:
            return 'Вот ' + str(c) + 'килограмм шерсти'
        else:
            return "У меня нет " + str(c) + ' килограмм шерсти. Вот только '+str(self.max_wool)+' килограмм'
        
    
class pig(Mammals):
    voice = 'Хрю'


class goat(Mammals):
    voice = 'Меее'


class Duck(Bird):
    voice = 'Кря'
    fly = True


class Chicken(Bird):
    voice = 'Кукареку'
    eggs = 0
    fly = False

    def get_egg(self):
        if self.eggs == 0:
            self.eggs += 1
            return 1
        else:
            return "Я сегодня уже давала яйца"
        

class Gees(Bird):
    voice = 'Гага'
    fly = True


d1 = Duck()
d1.make_voice()
c1 = Cow()
print('Получено молока,л:', c1.get_milk('Трава', 10))
print(c1.get_milk('Покрышки', 10))
ch = Chicken()
print(ch.get_egg())
print(ch.get_egg())
s1 = Sheep()
print(s1.get_wool(4))
print(s1.get_wool(20))
