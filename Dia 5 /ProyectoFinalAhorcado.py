
from random import choice

#Lista de Palabras para el ahorcado
def crear_palabras():
    palabras = [
        'Buseta',
        'Camion',
        'Bicicleta',
        'Patin'
    ]

    return palabras

#Crear Palabra Oculta 
def crear_palabra_oculta(palabra):
    
    mascara = ''
    for caracter in palabra:
        mascara += '_'
    
    return mascara
    

#Validar ingreso de usuario
def validar_letra(letra,palabra):

    return letra in palabra
        


#Ubicar Letra dentro de palabra
def ubicacion_letra(letra,palabra):
    return palabra.find(letra)


#Buscar y reemplazar la letra para mostrar al usuario
def reemplazar_letra(mascara,pos,letra):
    lista_mascara = list(mascara)

    i = int(pos)
    lista_mascara[i] = letra
    
    mascara = "".join(lista_mascara)
    return mascara

#Descontar vida
def descontar_vida(vidas):
    vidas -= 1
    return vidas

#Mostrar avance de palabra 
def  mostrar_mascara(palabra):
    print(f'La palabra hasta el momento es -> {palabra}')

#Jugar al ahorcado
def jugar():

    #Numero de vidas o intentos antes de morir
    vidas = 10

    palabra = choice(crear_palabras())
    palabra_oculta = crear_palabra_oculta(palabra)

    print(f'La palabra oculta es la siguiente: {palabra_oculta} y tiene {len(palabra_oculta)} espacios ')

    while vidas > 0:
        
        vidas = descontar_vida(vidas)
        
        letra = input('Ingrese letra a adiviar: ')


        if validar_letra(letra,palabra)==False:
            print(f'Letra no existe en palabra, le quedan {vidas} vidas, intente de nuevo')
            continue

        posicion_letra = ubicacion_letra(letra,palabra)
        palabra_oculta = reemplazar_letra(palabra_oculta,posicion_letra,letra)  
        mostrar_mascara(palabra_oculta)

        if palabra_oculta==palabra:
            print(f'¡Felicidades, haz ganado el juego adivinando la palabra -> {palabra}')
            break

    else:
        print('-'*100)
        print('Fin del juego')


#Configurar juego
print('Bienvenido al juego del ahorcado: \n ')
jugar()
