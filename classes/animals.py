class animal:
    voice = ''
    def make_voice(self):
        print (self.voice)
        
    pass
class bird(animal):
    fly = None
    pass
class mammals(animal):
    pass
class cow(mammals):
    voice='Moooo'
    pass
class sheep(mammals):
    voice='beee'
    max_wool=5
    def get_wool(self,c):
        if c<=self.max_wool:
            return 'Here is '+ str(c) +'kilo of wool'
        else:
            return "I have not "+ str(c) + ' kilo of wool,here is only '+str(self.max_wool)+' kilo'  
        
    pass
class pig(mammals):
    voice='Hriu'
    pass
class goat(mammals):
    voice='Mmmmee'
    pass
class duck(bird):
    voice='KriaKria'
    fly=True
    pass
class chicken(bird):
    voice='Kukarekooo'
    fly=False
    pass
class gees(bird):
    voice='Gagaga'
    fly=True
    pass

s1=sheep()
print(s1.get_wool(7))



