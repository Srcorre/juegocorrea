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
        super().__init__(6,6,50, 'Elfo')    #(ataque ,velocidad ,defensa, nombre)

class Humano(Raza): 
    def __init__(self):
        super().__init__(8,4,70, 'Humano')  

class Enano(Raza): 
    def __init__(self): 
        super().__init__(10,3,90, 'Enano')  

class Goblin(Raza): 
    def __init__(self): 
        super().__init__(10,3,90, 'Goblin') 

class Demonio(Raza): 
    def __init__(self): 
        super().__init__(100000,1000,1000000, 'Demonio') 

class Dios(Raza): 
    def __init__(self): 
        super().__init__(100000,1000,1000000, 'Dios') 
        
class Vampiro(Raza):                                     #NOMBRE TODAVIA NO CLARO
    def __init__(self): 
        super().__init__(100000,1000,1000000, 'Vampiro') 

#ELEMENTO

class Elemento:
    def __init__(self, ataque, velocidad, defensa, nombre):   #clase elemento
        self.elementoataque = ataque
        self.elementovelocidad = velocidad
        self.elementodefensa = defensa
        self.elementonombre = nombre                    #4 attributes

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
        super().__init__(0,0,10, 'Agua') 

class Aire(Elemento): 
    def __init__(self):  #(a,s,d)
        super().__init__(0,10,0, 'Aire') 

 

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
        super().__init__(0,4,5, 'Arco de Madera')    

class VaraDeMadera (Arma):   
    def __init__(self):
        super().__init__(4,-1,-5, 'Vara de Madera')   
    
class Garrote (Arma):         
    def __init__(self):
        super().__init__(6,-3,-10, 'Garrote')

class Tirachinas (Arma):         
    def __init__(self):
        super().__init__(2,5,-10, 'Tirachinas')          

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
        super().__init__(4,2,-5, 'Guerrero')          

class Tirador(Clase): 
    def __init__(self):
        super().__init__(4,1,0, 'Tirador')          

class Mago(Clase):    
    def __init__(self):
        super().__init__(0,5,10, 'Mago')            


                                                                                    #JUGADOR#
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
        print('\nTu personaje', self._protanombre.title(),' de genero ',self._protasexo ,'es un', self._protarace.returnNombre(), self._protaclass.returnClaseNombre(), 'con', self._protaarma.ReturnArmaNombre(),' y con el elemento ',self._protaelemento.returnElementoNombre())
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

def chooseNombre():
    nombre=input("Ponle un nombre a tu personaje: ")
    return nombre
    
def chooseSexo():
    opcion = ' '
    while not ('a' <= opcion <= 'b'):
     print("Elige el sexo de tu personaje: ")
     print("a) Hombre")
     print("b) Mujer")
     opcion=str(input("Escoje una opcion: "))
     if not (opcion == "a" or opcion == "b"):
      print("Solo puedes escojer una opcion entre a, b o c. Intentalo de nuevo: ")
     if opcion=='a':
      sexo="Hombre"
     elif opcion=='b':
      sexo="Mujer"
    return sexo


def chooseRaza():
        print("""
Razas:
a) Elfo
b) Humano
c) Enano
 """)
        
        choice = input("Elige una raza: ")
        while choice not in ['a','b','c']:      
            choice = input("Intentalo otra vez. (a,b o c): ")
        time.sleep(0.5)
        if choice == 'a':
            raza_ = Elfo()
        elif choice == 'b':
            raza_ = Humano()
        elif choice == 'c':
            raza_ = Enano()
        return raza_

def chooseClase():
    print("""
Clases:
a) Guerrero
b) Tirador
c) Mago
""")
    choice = input("Elige una Clase: ")
    while choice not in ['a','b','c']:
        choice = input("Solo puedes escojer una opcion entre a, b o c. Intentalo de nuevo: ")
    time.sleep(0.5)
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
       arma_ = VaraDeMadera() 
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
        print('\nEl enemigo es:', self._enemigorace.returnNombre(), self._enemigoclass.returnClaseNombre(), 'armado con', self._enemigoarma.ReturnArmaNombre())
        print('Ataque del enemigo:', self._enemigoataque)
        print('Velocidad del enemigo:', self._enemigovelocidad)
        print('Defensa del enemigo:', self._enemigodefensa, '\n')
        time.sleep(1)

def EnemigoRaza():
        races=[Elfo(), Humano(), Enano(), Goblin()]
        eraza = random.choice(races)
        return eraza
  
def Enemigoclass():
    classes=[Guerrero(), Mago(), Tirador()]
    enemigoclass = random.choice(classes)
    return enemigoclass       

def Enemigoarma(eclase):
    global earma_
    if eclase=="Guerrero":
       LGarma=[EspadaOxidada(), Garrote()]
       earma_ = random.choice(LGarma)
    elif eclase=="Tirador":
       LTarma=[Tirachinas(), ArcoDeMadera()]
       earma_ = random.choice(LTarma)
    elif eclase=="Mago":
       earma_ = VaraDeMadera() 
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

titulo = "bienvenido al mundo de XXXXXXXX".capitalize() 
print (titulo.center(100, "=")) 
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

enemigoraza= EnemigoRaza()                              #saca el arma del enemigo
enemigoclass = Enemigoclass()                           #saca la clase del enemigo
claseEn= enemigoclass.classnombre                       #mete la clase del enemigo en una variable para sacar el arma
enemigoarma = Enemigoarma(claseEn)                      #saca el arma del enemigo
enemigo=Enemigo(enemigoraza, enemigoclass, enemigoarma) #agrega la raza, la clase y el arma al enemigo
enemigo.CalculoPoderEnemigo()                           #calcula el poder total del enemigo
enemigo.printenemigostats()                             #saca las stats del enemigo




print('Tu salud actual:', prota._totaldefensa)
print('Salud actual del enemigo:', enemigo._enemigodefensa)                   #print prota/enemigo new saluds
print('El combate comienza...')
time.sleep(1)

while prota._totaldefensa >0 and enemigo._enemigodefensa >0:
    prota._totaldefensa -= (enemigo._enemigoataque*enemigo._enemigovelocidad) #prota salud - (enemigo velocidad * enemigo ataque)
    enemigo._enemigodefensa -= (prota._totalataque*prota._totalvelocidad)     #enemigo salud - (prota velocidad * prota ataque)
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

prota.Curar()                                           #Cura al personaje principal
enemigoraza= EnemigoRaza()                              #saca el arma del enemigo
enemigoclass = Enemigoclass()                           #saca la clase del enemigo
claseEn= enemigoclass.classnombre                       #mete la clase del enemigo en una variable para sacar el arma
enemigoarma = Enemigoarma(claseEn)                      #saca el arma del enemigo
enemigo=Enemigo(enemigoraza, enemigoclass, enemigoarma) #agrega la raza, la clase y el arma al enemigo
enemigo.CalculoPoderEnemigo()                           #calcula el poder total del enemigo
enemigo.printenemigostats()                             #saca las stats del enemigo


print('Tu salud actual:', prota._totaldefensa)
print('Salud actual del enemigo:', enemigo._enemigodefensa)                     #print prota/enemigo new saluds
print('El combate comienza...')
time.sleep(1)

while prota._totaldefensa >0 and enemigo._enemigodefensa >0:
    prota._totaldefensa -= (enemigo._enemigoataque*enemigo._enemigovelocidad)   #prota salud - (enemigo velocidad * enemigo ataque)
    enemigo._enemigodefensa -= (prota._totalataque*prota._totalvelocidad)       #enemigo salud - (prota velocidad * prota ataque)
    print('Tu Salud ', prota._totaldefensa)
    print('Salud del enemigo ', enemigo._enemigodefensa, '\n')
    time.sleep(1)
    
if prota._totaldefensa <0 and enemigo._enemigodefensa <0: 
    print('Empate, mataste a tu enemigo pero muriste en el acto')
    sys. exit()
elif prota._totaldefensa >0 and enemigo._enemigodefensa <0: 
    print('Ganaste!')
else:
    print('Has muerto!')   #Usar para acabar con el script: sys. exit()
    sys. exit()

'''

##################################################################################
#                                              BATALLAS                          #
##################################################################################


enemigoraza= EnemigoRaza()                              #saca el arma del enemigo
enemigoclass = Enemigoclass()                           #saca la clase del enemigo
claseEn= enemigoclass.classnombre                       #mete la clase del enemigo en una variable para sacar el arma
enemigoarma = Enemigoarma(claseEn)                      #saca el arma del enemigo
enemigo=Enemigo(enemigoraza, enemigoclass, enemigoarma) #agrega la raza, la clase y el arma al enemigo
enemigo.CalculoPoderEnemigo()                           #calcula el poder total del enemigo
enemigo.printenemigostats()                             #saca las stats del enemigo




print('Tu salud actual:', prota._totaldefensa)
print('Salud actual del enemigo:', enemigo._enemigodefensa)                   #print prota/enemigo new saluds
print('El combate comienza...')
time.sleep(1)

while prota._totaldefensa >0 and enemigo._enemigodefensa >0:
    prota._totaldefensa -= (enemigo._enemigoataque*enemigo._enemigovelocidad) #prota salud - (enemigo velocidad * enemigo ataque)
    enemigo._enemigodefensa -= (prota._totalataque*prota._totalvelocidad)     #enemigo salud - (prota velocidad * prota ataque)
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

prota.Curar()                                           #Cura al personaje principal
enemigoraza= EnemigoRaza()                              #saca el arma del enemigo
enemigoclass = Enemigoclass()                           #saca la clase del enemigo
claseEn= enemigoclass.classnombre                       #mete la clase del enemigo en una variable para sacar el arma
enemigoarma = Enemigoarma(claseEn)                      #saca el arma del enemigo
enemigo=Enemigo(enemigoraza, enemigoclass, enemigoarma) #agrega la raza, la clase y el arma al enemigo
enemigo.CalculoPoderEnemigo()                           #calcula el poder total del enemigo
enemigo.printenemigostats()                             #saca las stats del enemigo


print('Tu salud actual:', prota._totaldefensa)
print('Salud actual del enemigo:', enemigo._enemigodefensa)                     #print prota/enemigo new saluds
print('El combate comienza...')
time.sleep(1)

while prota._totaldefensa >0 and enemigo._enemigodefensa >0:
    prota._totaldefensa -= (enemigo._enemigoataque*enemigo._enemigovelocidad)   #prota salud - (enemigo velocidad * enemigo ataque)
    enemigo._enemigodefensa -= (prota._totalataque*prota._totalvelocidad)       #enemigo salud - (prota velocidad * prota ataque)
    print('Tu Salud ', prota._totaldefensa)
    print('Salud del enemigo ', enemigo._enemigodefensa, '\n')
    time.sleep(1)
    
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
