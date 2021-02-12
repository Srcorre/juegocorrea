
#ELEMENTO

class Elemento:
    def __init__(self, ataque, velocidad, defensa, nombre):   #element class
        self.elementoataque = ataque
        self.elementovelocidad = velocidad
        self.elementodefensa = defensa
        self.elementonombre = nombre                    #4 attributes of element class

    def returnElementoAtaque(self):
        return self.elementoataque
    def returnElementoVelocidad(self):
        return self.elementovelocidad
    def returnElementoDefensa(self):
        return self.elementodefensa
    def returnElementoNombre(self):
        return self.elementonombre


class Fuego(Elemento): 
    def __init__(self):
        super().__init__(10,0,0, 'Fuego') #(ataque ,velocidad ,defensa, nombre)

class Agua(Elemento): 
    def __init__(self):
        super().__init__(0,0,10, 'Agua') #(ataque ,velocidad ,defensa, nombre)

class Aire(Elemento): 
    def __init__(self):  #(a,s,d)
        super().__init__(0,10,0, 'Aire') #(ataque ,velocidad ,defensa, nombre)
