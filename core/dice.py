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
    
    def comenzar(self):
        empate = 0
        while empate == 0:
            self.dado_1 = random.randint(1,6)
            resultado_1 = self.dado_1 
            self.dado_2 = random.randint(1,6)
            resultado_2 = self.dado_2
            if resultado_1 == resultado_2:
                empate = 0
            else:
                empate = 1
        if resultado_1 > resultado_2:
            print("Empiezan las fichas blancas")
        else: 
            print("Empiezan las fichas negras")
