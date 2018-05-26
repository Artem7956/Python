class animal:
    voice = ''
    ration = ''

    def make_voice(self):
        print(self.voice)
        
    pass
class bird(animal):
    ration='Зерно'
    fly = None
    pass
class mammals(animal):
    ration='Трава'
    pass
class cow(mammals):
    voice='Му'
    
    def get_milk(self,r,c):# r-рацион,c-количество травы. Возвращает n - литров молока по формуле n=c/2
        if r==self.ration: 
            return c/2
        else:
            return 'Я не ем '+ r

        

    
    pass
class sheep(mammals):
    voice='Бееее'
    max_wool=5
    def get_wool(self,c):
        if c<=self.max_wool:
            return 'Вот '+ str(c) +'килограмм шерсти'
        else:
            return "У меня нет "+ str(c) + ' килограмм шерсти. Вот только '+str(self.max_wool)+' килограмм'  
        
    pass
class pig(mammals):
    voice='Хрю'
    pass
class goat(mammals):
    voice='Меее'
    pass
class duck(bird):
    voice='Кря'
    fly=True
    pass
class chicken(bird):
    voice='Кукареку'
    eggs=0
    
    fly=False
    def get_egg(self):
        if self.eggs==0 :
            self.eggs+=1
            return 1
        else: return "Я сегодня уже давала яйца"
        
    
    pass
class gees(bird):
    voice='Гага'
    fly=True
    pass
d1=duck()
d1.make_voice()
c1=cow()
print('Получено молока,л:',c1.get_milk('Трава',10))
print(c1.get_milk('Покрышки',10))
ch=chicken()
print(ch.get_egg())
print(ch.get_egg())


s1=sheep()
print(s1.get_wool(4))

print(s1.get_wool(20))



