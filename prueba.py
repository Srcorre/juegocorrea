import time             #importing necessary libraries
import random
import sys

#RAZA#
class Raza:
    def __init__(self, ataque, velocidad, defensa, nombre):   #clase raza
        self.ataque = ataque
        self.velocidad = velocidad
        self.defensa = defensa
        self.nombre = nombre                    #4 atributos

    def returnAtaque(self):
        return self.ataque
    def returnVelocidad(self):
        return self.velocidad
    def returnDefensa(self):
        return self.defensa
    def returnNombre(self):
        return self.nombre


class Elfo(Raza): #inherits from race
    def __init__(self):
        super().__init__(6,6,50, 'Elfo') #(ataque ,velocidad ,defensa, nombre)

class Humano(Raza): #inherits from race
    def __init__(self):
        super().__init__(8,4,70, 'Humano') #(ataque ,velocidad ,defensa, nombre)

class Enano(Raza): #inherits from race
    def __init__(self):  #(a,s,d)
        super().__init__(10,3,90, 'Enano') #(ataque ,velocidad ,defensa, nombre)


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


class Fuego(Elemento): #inherits from race
    def __init__(self):
        super().__init__(10,0,0, 'Fuego') #(ataque ,velocidad ,defensa, nombre)

class Agua(Elemento): #inherits from race
    def __init__(self):
        super().__init__(0,0,10, 'Agua') #(ataque ,velocidad ,defensa, nombre)

class Aire(Elemento): #inherits from race
    def __init__(self):  #(a,s,d)
        super().__init__(0,10,0, 'Aire') #(ataque ,velocidad ,defensa, nombre)

 

#ARMAS#
class Arma:
    def __init__(self, ataque, velocidad, defensa, nombre):
        self.armaataque = ataque
        self.armavelocidad = velocidad
        self.armadefensa = defensa
        self.armanombre = nombre              #4 attributes of arma class

    def ReturnArmaAtaque(self):
        return self.armaataque
    def ReturnArmaVelocidad(self):
        return self.armavelocidad
    def ReturnArmaDefensa(self):
        return self.armadefensa
    def ReturnArmaNombre(self):
        return self.armanombre

class EspadaOxidada (Arma): #inherits from arma
    def __init__(self):
        super().__init__(1,1,10, 'EspadaOxidada') #(ataque ,velocidad ,defensa, nombre)

class ArcoDeMadera (Arma):   
    def __init__(self):
        super().__init__(0,4,5, 'ArcoDeMadera')    

class Vara (Arma):   
    def __init__(self):
        super().__init__(4,-1,-5, 'Vara')   
    
class Gun (Arma):         
    def __init__(self):
        super().__init__(6,-3,-10, 'Gun')     

class SableDeDios (Arma):    
    def __init__(self):
        super().__init__(6,30,100, 'Sable')        

#CLASES#
class ProtaClase:
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


class Guerrero(ProtaClase): #inherits from characterclass     
    def __init__(self):
        super().__init__(4,2,-5, 'Guerrero')             #(ataque ,velocidad ,defensa, nombre)

class Tirador(ProtaClase): #inherits from characterclass
    def __init__(self):
        super().__init__(4,1,0, 'Tirador')            #(ataque ,velocidad ,defensa, nombre)

class Mago(ProtaClase):    #inherits from characterclass
    def __init__(self):
        super().__init__(0,5,10, 'Mago')            #(ataque ,velocidad ,defensa, nombre)


##
class Player:

    def __init__(self, protaClase, protaArma, protaElemento):
        self._totalataque = 0
        self._totalvelocidad = 0
        self._totaldefensa = 0
        self._protarace = ''
        self._protaclass = protaClase 
        self._protaarma = protaArma
        self._protaelemento = protaElemento        
            
    def chooseRaza(self):
        print("""
Razas:
a. Elfo - Ataque: 6, Velocidad: 6, Defensa: 50
b. Humano - Ataque: 8, Velocidad: 4, Defensa: 70
c. Enano - Ataque: 10, Velocidad: 3, Defensa: 90
 """)
        
        choice = input("Choose a race:")
        while choice not in ['a','b','c']:      
            choice = input("Intentalo otra vez. (a,b o c)")
        time.sleep(0.5)
        if choice == 'a':
            self._protarace = Elfo()
        elif choice == 'b':
            self._protarace = Humano()
        elif choice == 'c':
            self._protarace = Enano()            

        self._totalataque += self._protarace.returnAtaque() + self._protaclass.returnClaseAtaque() + self._protaarma.ReturnArmaAtaque() + self._protaelemento.returnElementoAtaque()
        self._totalvelocidad += self._protarace.returnVelocidad() + self._protaclass.returnClaseVelocidad() + self._protaarma.ReturnArmaVelocidad()+ self._protaelemento.returnElementoVelocidad()
        self._totaldefensa += self._protarace.returnDefensa() + self._protaclass.returnClaseDefensa() + self._protaarma.ReturnArmaDefensa()+self._protaelemento.returnElementoDefensa()

    def printstats(self):
        print('\nTu personaje es un', self._protarace.returnNombre(), self._protaclass.returnClaseNombre(), 'con', self._protaarma.ReturnArmaNombre(), self._protaelemento.returnElementoNombre)
        print('Prota Ataque:', self._totalataque)
        print('Prota Velocidad:', self._totalvelocidad)
        print('Prota Defensa:', self._totaldefensa)

    



def chooseClase():
    print("""
Clases:
a. Guerrero
b. Tirador
c. Mago
""")
    choice = input("Elige una Clase:")
    while choice not in ['a','b','c']:
        choice = input("Intentalo de nuevo con: (a,b o c)")
    time.sleep(0.5)
    if choice == 'a':
        class_ = Guerrero()
    elif choice == 'b':
        class_ = Tirador()
    elif choice == 'c':
        class_ = Mago()
    return class_

def chooseElemento():
    choice = input("Elige un elemento:")
    while choice not in ['a','b','c']:
        choice = input("Intentalo de nuevo con: (a, b o c)")
    time.sleep(0.5)
    if choice == 'a':
        elemento_=Fuego()
    elif choice == 'b':
        elemento_=Agua()
    elif choice == 'c':
        elemento_=Aire()
    return elemento_
    
     

   
def chooseArma():
    print("""
Armas:
1. SwordShield - Ataque: 1, Velocidad: 1, Defensa: 10
2. DualSword - Ataque: 0, Velocidad: 4, Defensa: 5
3. BowArrow - Ataque: 4, Velocidad: -1, Defensa: -5
4. Gun - Ataque: 6, Velocidad: -3, Defensa: -10
""")
    choice = input("Elige un arma:")
    while choice not in ['1','2','3','4']:
        choice = input("Intentalo de nuevo con: (1,2,3 or 4)")
    time.sleep(0.5)
    if choice == '1':
        arma_ = EspadaOxidada()
    elif choice == '2':
        arma_ = ArcoDeMadera()
    elif choice == '3':
        arma_ = Vara()
    elif choice == '4':
        arma_ = Gun()
    return arma_




class Enemigo:
    def __init__(self, enemigoclass, enemigoarma):
        self._enemigoataque = 0
        self._enemigodefensa = 0
        self._enemigovelocidad = 0
        self._enemigorace = ''
        self._enemigoarma = enemigoarma
        self._enemigoclass = enemigoclass

    def EnemigoRaza(self):
        races=[Elfo(), Humano(), Enano()]
        self._enemigorace = random.choice(races)

        self._enemigoataque += self._enemigorace.returnAtaque() + self._enemigoclass.returnClaseAtaque() + self._enemigoarma.ReturnArmaAtaque()
        self._enemigovelocidad += self._enemigorace.returnVelocidad() + self._enemigoclass.returnClaseVelocidad() + self._enemigoarma.ReturnArmaVelocidad()
        self._enemigodefensa += self._enemigorace.returnDefensa() + self._enemigoclass.returnClaseDefensa() + self._enemigoarma.ReturnArmaDefensa()
        

    def printenemigostats(self):
        #print('\nGenerating a random enemigo...')
        #time.sleep(1)
        print('\nEl enemigo es:', self._enemigorace.returnNombre(), self._enemigoclass.returnClaseNombre(), 'armado con', self._enemigoarma.ReturnArmaNombre())
        print('Ataque del enemigo:', self._enemigoataque)
        print('Velocidad del enemigo:', self._enemigovelocidad)
        print('Defensa del enemigo:', self._enemigodefensa, '\n')
        time.sleep(1)

  
def enemigoclass():
    classes=[Guerrero(), Mago(), Tirador()]
    enemigoclass = random.choice(classes)
    return enemigoclass       #randomly picks enemigo class

def enemigoarma():
    armas=[EspadaOxidada(), ArcoDeMadera(), Vara(), Gun()]
    enemigoarma = random.choice(armas)
    return enemigoarma      #randomly picks enemigo arma
    
#LISTAS

listaH_H = ["Luos", "Wulf" , "Agabo", "Canuto"]
listaH_Elf = ["Luos", "Ilvo", "Dantel", "Duilio", "Alfe"]
listaH_En = ["Volgo", "Agabo", "Borge"]
listaM_H = ["Luna" , "Joana" , "Vella", "Elicia", "Siraina"]
listaM_Elf =["Luna", "Veyal", "Shelia", "Maira"]
listaM_En = [ "Ilga", "Babila", "Davina"]
'''
#PAREJA

if(sexo=="hombre" and raza=="humano"):
 pareja=str(random.choice(listaM_H))
elif(sexo=="mujer" and raza=="humano"):
 pareja=str(random.choice(listaH_H))
 
elif(sexo=="hombre" and raza=="elfo"):
 pareja=str(random.choice(listaM_Elf))
elif(sexo=="mujer" and raza=="elfo"):
 pareja=str(random.choice(listaH_Elf))
 
elif(sexo=="hombre" and raza=="enano"):
 pareja=str(random.choice(listaM_En))
elif(sexo=="mujer" and raza=="enano"):
 pareja=str(random.choice(listaH_En))
'''

protaClase=chooseClase()
protaElemento=chooseElemento()
protaArma=chooseArma()
prota=Player(protaClase,protaElemento, protaArma)
prota.chooseRaza()
prota.printstats()

'''

##################################################################################
#APARTIR DE AQUI DEJA DE DEFINIR FUNCIONES Y CLASES                              #
##################################################################################

protaClase=chooseClase() #gets the protas class
protaArma=chooseArma() #gets the protas arma

prota=Player(protaClase, protaArma) #prota is object of player class
prota.chooseRaza() #prota choosses player race
prota.printstats() #prints protas stats


enemigoclass = enemigoclass() #gets enemigo class
enemigoarma = enemigoarma() #gets enemigo arma

enemigo=Enemigo(enemigoclass, enemigoarma) #aggregation takes place
enemigo.EnemigoRaza()
enemigo.printenemigostats() #prints enemigo stats


#Combat Section
numbers = [1,2,3,4,5]
prota._totaldefensa = prota._totaldefensa*random.choice(numbers) #randomly multiplies salud of prota and enemigo by 1-5
enemigo._enemigodefensa = enemigo._enemigodefensa*random.choice(numbers) #randomly multiplies salud of prota and enemigo by 1-5
print('Tu salud actual:', prota._totaldefensa)
print('Salud actual del enemigo:', enemigo._enemigodefensa) #print prota/enemigo new saluds
print('El combate comienza...')
time.sleep(1)

while prota._totaldefensa >0 and enemigo._enemigodefensa >0:
    prota._totaldefensa -= (enemigo._enemigoataque*enemigo._enemigovelocidad) #prota salud - (enemigo velocidad * enemigo ataque)
    enemigo._enemigodefensa -= (prota._totalataque*prota._totalvelocidad) #enemigo salud - (prota velocidad * prota ataque)
    print('Tu Salud ', prota._totaldefensa)
    print('Salud del enemigo ', enemigo._enemigodefensa, '\n')
    time.sleep(1) #wait a second till the next turn
    
if prota._totaldefensa <0 and enemigo._enemigodefensa <0: 
    print('Empate, mataste a tu enemigo pero muriste en el acto')
elif prota._totaldefensa >0 and enemigo._enemigodefensa <0: 
    print('Ganaste!')
else:
    print('Has muerto!')   #Usar para acabar con el script: sys. exit()
    
'''

