
## Adivinanzas para el juego de azar! 
from random import randint


#Numero de intentos 
intentos = 0

#Preguntar por el nombre del jugador
nombre_jugador = input("Por favor introduzca su nombre -> ")

#Bienvenida al usuario 
print(f"¡Hola {nombre_jugador}! Bienvenido al juego de Azar, Vamos a configurar el juego")
print("-"*100)

#Configuración del juego 
intentos = int(input('¿Cuantos intentos desea jugar el día de hoy? -> '))
print("-"*100)

max_numero = int(input('¿Hasta que número desea jugar el día de hoy? -> '))
print("-"*100)

#Reglas del juego 
print(f"Vamos a intentar adivinar un numero entre 1 y {max_numero}, tienes solo {intentos} intentos para lograr adivinar. ¡Comencemos!")
print("\n")

#Generar numero random 
numero_random = randint(1,max_numero)
veces = 0 

while intentos > 0:

    numero = int(input(f"Numero de intentos restantes '{intentos}', Ingrese el numero a adivinar -> "))

    match numero:
        case _ if (numero < 1 or numero > max_numero):
            print("Numero fuera de rango")
        case _ if (numero < numero_random):
            print("No es el correcto, El numero es menor al ingresado ")
        case _ if (numero > numero_random):
            print("No es el correcto, El numero es mayor al ingresado ")
        case _ if (numero == numero_random):
            print(f"¡Felicitadades, haz acertado el numero y lo hicistes en '{veces}' intentos. Gracias")
            break

    print("\n")
    intentos -= 1
    veces += 1


else:
    print(f"Fin del juego. El numero a adivinar era el {numero_random}. Gracias por jugar")

    