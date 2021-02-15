import time             
import random
import sys
from func import *

#LISTAS

listaH_H = ["Luos", "Wulf" , "Agabo", "Canuto"]
listaH_Elf = ["Luos", "Ilvo", "Dantel", "Duilio", "Alfe"]
listaH_En = ["Volgo", "Agabo", "Borge"]
listaM_H = ["Luna" , "Joana" , "Vella", "Elicia", "Siraina"]
listaM_Elf =["Luna", "Veyal", "Shelia", "Maira"]
listaM_En = [ "Ilga", "Babila", "Davina"]

   
edad=random.randint(14,18)   

titulo = "bienvenido al mundo de XXXXXXXX".capitalize() 
print (titulo.center(100, "=")) 
protaRaza=chooseRaza()   
protaClase=chooseClase()
clase=protaClase.classnombre
protaArma=chooseArma(clase)
protaNombre=chooseNombre()
protaSexo=chooseSexo()
prota=Player(protaRaza, protaClase, protaArma,  protaNombre, protaSexo)
prota.CalculoPoder()
raza=prota.sacarRaza()



if raza=="Elfo":
 exec(open("elfo.py").read())
elif raza=="Enano":
 exec(open("enano.py").read())
elif raza=="Humano":
 exec(open("humano.py").read())
