# Esta clase corresponde a todos los detalles del jugador. Deberia ser creada la primera de todas.
# Separar los objectos en documentos diferentes e importarlos a traves de ellos cuando sea necesario para mantener el codigo limpio y estructurado


import Raza
import Tipo
import Elementos
import Arma

import random

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


    def chooseRaza():
        print('Elige una raza: \na) Elfo \nb) Humano \nc) Enano')
        choice = input("> ")
        choice = choice.lower()
        while choice not in ['a','b','c']:      
            choice = input("Opcion invalida. Prueba otra vez: \n>  ")
        if choice == 'a':
            raza_ = Raza.Elfo()
        elif choice == 'b':
            raza_ = Raza.Humano()
        elif choice == 'c':
            raza_ = Raza.Enano()
        return raza_


    def chooseSexo():
        print("Elige el sexo de tu personaje: \na) Hombre \nb) Mujer \n") 
        while True:
            choice = input("> ")
            choice = choice.lower()
            if choice == 'a':
                sexo = 'Hombre'
                break
            elif choice == 'b':
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
        choice = choice.lower()
        while choice not in ['a','b','c']:      
            choice = input("Solo puedes escojer una opcion entre a, b o c. Intentalo de nuevo:\n>  ")
        if choice == 'a':
            class_ = Tipo.Guerrero()
        elif choice == 'b':
            class_ = Tipo.Tirador()
        elif choice == 'c':
            class_ = Tipo.Mago()
        return class_



    # ELEMENTO + libreria random

    def chooseElemento():
        cont=str(random.randint(1,3))
        if cont == '1':
            elemento_= Elementos.Fuego()
        elif cont == '2':
            elemento_= Elementos.Agua()
        elif cont == '3':
            elemento_= Elementos.Aire()
        return elemento_
        
    # ARMA

    def chooseArma():
        if clase == "Guerrero":
           arma = Arma.SableDeDios()
           return arma
        elif clase == "Tirador":
           arma = Arma.ArcoDeMadera()
           return arma 
        elif clase == "Mago":
           arma = Arma.Vara()
           return arma 


raza = Player.chooseRaza()
sexo = Player.chooseSexo()
nombre = Player.chooseNombre()
clase = Player.chooseClase()
elemento = Player.chooseElemento()
arma = Player.chooseArma()

print("-----------------------------")
print(f"raza: {raza} \nsexo: {sexo} \nnombre: {nombre} \nclase: {clase} \nelemento: {elemento} \narma: {arma}")
print("-----------------------------")
