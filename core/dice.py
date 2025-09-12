import random

class Dados:
    def __init__(self, __dado_1__, __dado_2__):
        self.dado_1 = __dado_1__
        self.dado_2 = __dado_2__
    
    def tirar_dado(self):
        self.dado_1 = random.randint(1,6)
        self.dado_2 = random.randint(1,6)
        if self.dado_1 == self.dado_2:
            return[self.dado_1,self.dado_2,self.dado_1,self.dado_2]
        else:
            return[self.dado_1, self.dado_2]