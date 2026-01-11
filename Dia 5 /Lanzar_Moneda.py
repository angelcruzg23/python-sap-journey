
from random import choice

def lanzar_moneda()
    
    moneda = ['Cara','Cruz']
    
    return choice(moneda) 

def probar_suerte(moneda,lista_numeros):

    if moneda=='Cara':
        print('La lista se autodestruirá')
        return lista_numeros.clear()
    else:
        print('La lista fue salvada')

    return lista_numeros


