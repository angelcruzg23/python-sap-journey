
from random import shuffle

palitos = ['-','--','---','----']


#Mezclar palitos 
def mezclar_palitos(palitos):
    shuffle(palitos)
    return palitos

#Obtener seleccion
def obtener_seleccion_usuario():
    
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero entre 1 y 4 para ver si te toca el palito largo: ')
    
    return intento

#Validar seleccion
def validar_seleccion(palitos_mezclados,intento_usuario):

    palito_largo = '----'
    palito_seleccionado = palitos_mezclados[int(intento_usuario) - 1]

    if palito_largo == palito_seleccionado:
        print("Te ganaste el premio")
    else:
        print(f'Sigue intentando, tu selección fue: {palito_seleccionado}')


#Ejecutar programa 
validar_seleccion(mezclar_palitos(palitos),obtener_seleccion_usuario())
                  