
#desde libreria importa metodo
#from random import randint 
#from random import * 

from random import *

aleatorio = randint(1,500) #-> Int 
print(aleatorio)

aleatorio = uniform(1,50) #-> Float 
print(aleatorio)

aleatorio = round(uniform(1,50),2) #-> Float con 1 Decimal 
print(aleatorio)

colores = ['Blanco','Azul','Rojo','Amarillo','Verder']
aleatorio = choice(colores)
print(aleatorio)

#Desordenar una lista X
numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)
