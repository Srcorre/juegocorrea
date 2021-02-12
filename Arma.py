#ARMAS#
class Arma:
    def __init__(self, ataque, velocidad, defensa, nombre):
        self.armaataque = ataque
        self.armavelocidad = velocidad
        self.armadefensa = defensa
        self.armanombre = nombre              

    def ReturnArmaAtaque(self):
        return self.armaataque
    def ReturnArmaVelocidad(self):
        return self.armavelocidad
    def ReturnArmaDefensa(self):
        return self.armadefensa
    def ReturnArmaNombre(self):
        return self.armanombre

class EspadaOxidada (Arma): 
    def __init__(self):
        super().__init__(1,1,10, 'Espada Oxidada') #(ataque ,velocidad ,defensa, nombre)

class ArcoDeMadera (Arma):   
    def __init__(self):
        super().__init__(0,4,5, 'Arco De Madera')    

class Vara (Arma):   
    def __init__(self):
        super().__init__(4,-1,-5, 'Vara')   
    
class Gun (Arma):         
    def __init__(self):
        super().__init__(6,-3,-10, 'Gun')     

class SableDeDios (Arma):    
    def __init__(self):
        super().__init__(100,30,2000, 'Sable de dios')        