# Tipo de clase: Guerrero, Tirador y Mago

class Clase:
    def __init__(self, ataque, velocidad, defensa, nombre):
        self.classataque = ataque
        self.classvelocidad = velocidad
        self.classdefensa = defensa
        self.classnombre = nombre

    def returnClaseAtaque(self):
        return self.classataque
    def returnClaseVelocidad(self):
        return self.classvelocidad
    def returnClaseDefensa(self):
        return self.classdefensa
    def returnClaseNombre(self):
        return self.classnombre


class Guerrero(Clase):   
    def __init__(self):
        super().__init__(4,2,-5, 'Guerrero')             #(ataque ,velocidad ,defensa, nombre)

class Tirador(Clase): 
    def __init__(self):
        super().__init__(4,1,0, 'Tirador')            #(ataque ,velocidad ,defensa, nombre)

class Mago(Clase):    
    def __init__(self):
        super().__init__(0,5,10, 'Mago')            #(ataque ,velocidad ,defensa, nombre)