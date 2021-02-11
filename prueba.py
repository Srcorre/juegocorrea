import time             
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


class Elfo(Raza): 
    def __init__(self):
        super().__init__(6,6,50, 'Elfo') #(ataque ,velocidad ,defensa, nombre)

class Humano(Raza): 
    def __init__(self):
        super().__init__(8,4,70, 'Humano') #(ataque ,velocidad ,defensa, nombre)

class Enano(Raza): 
    def __init__(self): 
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


class Fuego(Elemento): 
    def __init__(self):
        super().__init__(10,0,0, 'Fuego') #(ataque ,velocidad ,defensa, nombre)

class Agua(Elemento): 
    def __init__(self):
        super().__init__(0,0,10, 'Agua') #(ataque ,velocidad ,defensa, nombre)

class Aire(Elemento): 
    def __init__(self):  #(a,s,d)
        super().__init__(0,10,0, 'Aire') #(ataque ,velocidad ,defensa, nombre)

 

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

#CLASES#
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


##
class Player:

    def __init__(self, protaRaza ,protaClase, protaArma, protaElemento, protaNombre, protaSexo):
        self._totalataque = 0
        self._totalvelocidad = 0
        self._totaldefensa = 0
        self._protarace = protaRaza
        self._protaclass = protaClase 
        self._protaarma = protaArma
        self._protaelemento = protaElemento
        self._protanombre = protaNombre
        self._protasexo = protaSexo       
            
    def CalculoPoder(self):          
        self._totalataque += self._protarace.returnAtaque() + self._protaclass.returnClaseAtaque() + self._protaarma.ReturnArmaAtaque() + self._protaelemento.returnElementoAtaque()
        self._totalvelocidad += self._protarace.returnVelocidad() + self._protaclass.returnClaseVelocidad() + self._protaarma.ReturnArmaVelocidad()+ self._protaelemento.returnElementoVelocidad()
        self._totaldefensa += self._protarace.returnDefensa() + self._protaclass.returnClaseDefensa() + self._protaarma.ReturnArmaDefensa()+self._protaelemento.returnElementoDefensa()
    
    

    def printstats(self):
        print('\nTu personaje', self._protanombre,' de genero ',self._protasexo ,'es un', self._protarace.returnNombre(), self._protaclass.returnClaseNombre(), 'con', self._protaarma.ReturnArmaNombre(),' y con el elemento ',self._protaelemento.returnElementoNombre())
        print('Prota Ataque:', self._totalataque)
        print('Prota Velocidad:', self._totalvelocidad)
        print('Prota Defensa:', self._totaldefensa)
    
    def sacarRaza(self):
        raza=self._protarace.returnNombre()
        return raza
        
    def Curar(self):
        self._totaldefensa=0
        self._totaldefensa += self._protarace.returnDefensa() + self._protaclass.returnClaseDefensa() + self._protaarma.ReturnArmaDefensa()+self._protaelemento.returnElementoDefensa()

#NOMBRE    
# Crear Personaje   

def chooseRaza():
        print('Elige una raza: \na) Elfo \nb) Humano \nc) Enano')
        choice = input("> ")
        while choice.lower() not in ['a','b','c']:      
            choice = input("Opcion invalida. Prueba otra vez: \n>  ")
        if choice == 'a':
            raza_ = Elfo()
        elif choice == 'b':
            raza_ = Humano()
        elif choice == 'c':
            raza_ = Enano()
        return raza_


def chooseSexo():
	print("Elige el sexo de tu personaje: \na) Hombre \nb) Mujer \n") 
	while True:
		opcion = input("> ")
		if opcion.lower() == 'a':
			sexo = 'Hombre'
			break
		elif opcion.lower() == 'b':
			sexo = 'Mujer'
			break
		else:
			print('Opcion invalida, prueba otra vez')
	return sexo


def chooseNombre():
    nombre=input("Cual es tu nombre? \n> ")
    return nombre



def chooseClase():
    print('Elige una Clase: \na) Guerrero \nb) Tirador \nc) Mago')
    choice = input("> ")
    while choice.lower() not in ['a','b','c']:      
        choice = input("Solo puedes escojer una opcion entre a, b o c. Intentalo de nuevo:\n>  ")
    if choice == 'a':
        class_ = Guerrero()
    elif choice == 'b':
        class_ = Tirador()
    elif choice == 'c':
        class_ = Mago()
    return class_



#ELEMENTO

def chooseElemento():
    cont=str(random.randint(1,3))
    if cont == '1':
        elemento_=Fuego()
    elif cont == '2':
        elemento_=Agua()
    elif cont == '3':
        elemento_=Aire()
    return elemento_
    
     

def chooseArma(clase):
    if clase=="Guerrero":
       arma_ = SableDeDios()
    elif clase=="Tirador":
       arma_ = ArcoDeMadera() 
    elif clase=="Mago":
       arma_ = Vara() 
    return arma_       


'''
def chooseArma():
    print("""
Armas:
a) EspadaOxidada
b) ArcoDeMadera
c) Vara
d) Gun
""")
    choice = input("Elige un arma: ")
    while choice not in ['a','b','c','d']:
        choice = input("Solo puedes escojer una opcion entre a, b, c o d. Intentalo de nuevo: ")
    time.sleep(0.5)
    if choice == 'a':
        arma_ = EspadaOxidada()
    elif choice == 'b':
        arma_ = ArcoDeMadera()
    elif choice == 'c':
        arma_ = Vara()
    elif choice == 'd':
        arma_ = Gun()
    return arma_
'''
###################################################
#         ENEMIGOS                                #
###################################################
class Enemigo:
    def __init__(self, enemigoraza ,enemigoclass, enemigoarma):
        self._enemigoataque = 0
        self._enemigodefensa = 0
        self._enemigovelocidad = 0
        self._enemigorace = enemigoraza
        self._enemigoarma = enemigoarma
        self._enemigoclass = enemigoclass

    def CalculoPoderEnemigo(self):
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

def EnemigoRaza():
        races=[Elfo(), Humano(), Enano()]
        eraza = random.choice(races)
        return eraza
  
def Enemigoclass():
    classes=[Guerrero(), Mago(), Tirador()]
    enemigoclass = random.choice(classes)
    return enemigoclass       

def Enemigoarma(eclase):
    global earma_
    if eclase=="Guerrero":
       earma_ = EspadaOxidada()
    elif eclase=="Tirador":
       earma_ = ArcoDeMadera() 
    elif eclase=="Mago":
       earma_ = Vara() 
    return earma_        
    
#LISTAS

listaH_H = ["Luos", "Wulf" , "Agabo", "Canuto"]
listaH_Elf = ["Luos", "Ilvo", "Dantel", "Duilio", "Alfe"]
listaH_En = ["Volgo", "Agabo", "Borge"]
listaM_H = ["Luna" , "Joana" , "Vella", "Elicia", "Siraina"]
listaM_Elf =["Luna", "Veyal", "Shelia", "Maira"]
listaM_En = [ "Ilga", "Babila", "Davina"]



#MAESTRO   (dividir el argumento de 0 a 2, de 3 a 6 y 7 oculto)

num=random.randint(0,7)
if num==0:
  maestro="Vampiro"
elif num==1:
  maestro="Cambiapieles"
elif num==2:
  maestro="Bandido"
elif num==3:
  maestro="Paladin"
elif num==4:
  maestro="Pirata"
elif num==5:
  maestro="Nomada"
elif num==6:
  maestro="Mago"
elif num==7:
  mestro="Demonio"  
  
#EDAD     (Para llevar referencia del paso del tiempo)

edad=random.randint(14,18)   


protaRaza=chooseRaza()   
protaClase=chooseClase()
clase=protaClase.classnombre
protaArma=chooseArma(clase)
protaElemento=chooseElemento()
protaNombre=chooseNombre()
protaSexo=chooseSexo()
prota=Player(protaRaza, protaClase, protaArma, protaElemento, protaNombre, protaSexo)
prota.CalculoPoder()
prota.printstats()
raza=prota.sacarRaza()

#PAREJA
sexo=protaSexo
if(sexo=="Hombre" and raza=="Humano"):
 pareja=str(random.choice(listaM_H))
elif(sexo=="Mujer" and raza=="Humano"):
 pareja=str(random.choice(listaH_H))
 
elif(sexo=="Hombre" and raza=="Elfo"):
 pareja=str(random.choice(listaM_Elf))
elif(sexo=="Mujer" and raza=="Elfo"):
 pareja=str(random.choice(listaH_Elf))
 
elif(sexo=="Hombre" and raza=="Enano"):
 pareja=str(random.choice(listaM_En))
elif(sexo=="Mujer" and raza=="Enano"):
 pareja=str(random.choice(listaH_En))

print(sexo)
print(pareja)


print(protaClase.classnombre) 



'''

##################################################################################
#                                              BATALLAS                          #
##################################################################################



enemigoraza= EnemigoRaza()
enemigoclass = Enemigoclass() #gets enemigo class
claseEn= enemigoclass.classnombre
enemigoarma = Enemigoarma(claseEn) #gets enemigo arma
enemigo=Enemigo(enemigoraza, enemigoclass, enemigoarma) #aggregation takes place
enemigo.CalculoPoderEnemigo()
enemigo.printenemigostats() #prints enemigo stats




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
    sys. exit()
elif prota._totaldefensa >0 and enemigo._enemigodefensa <0: 
    print('Ganaste!')
else:
    print('Has muerto!')   #Usar para acabar con el script: sys. exit()
    sys. exit()
    
time.sleep(2)
print('Siguiente combate')
print(type(enemigoclass))
time.sleep(3)

prota.Curar()


enemigoraza= EnemigoRaza()
enemigoclass = Enemigoclass() #gets enemigo class
claseEn= enemigoclass.classnombre
enemigoarma = Enemigoarma(claseEn) #gets enemigo arma
enemigo=Enemigo(enemigoraza, enemigoclass, enemigoarma) #aggregation takes place
enemigo.CalculoPoderEnemigo()
enemigo.printenemigostats() #prints enemigo stats


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
    sys. exit()
elif prota._totaldefensa >0 and enemigo._enemigodefensa <0: 
    print('Ganaste!')
else:
    print('Has muerto!')   #Usar para acabar con el script: sys. exit()
    sys. exit()
'''

'''
###################################################################################
#                                HISTORIA                                         #
###################################################################################

print("Habia una vez un ",raza," llamado ", nombre, "que vivia en una pequeña ciudad llamada Argonia. Era un lugar tranquilo y apacible dirigido por un Señor Feudal considerado perfecto")
print('Alli ',nombre, ' conocio a:', pareja, ' con la cual crecio desde su mas tierna infacia')
print("En la escuela militar aprendio y acabo volviendose un buen ", clase, "y gracias a la prueba del papel descubrio que su elemento principal era el ", elemento)

'''
