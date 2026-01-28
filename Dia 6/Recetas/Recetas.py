
import os
from pathlib import Path

menuRecetas = ['1. Leer Recetas','2. Crear Receta','3. Crear Categoria','4. Eliminar Receta','5. Eliminar Categoria','6. Salir']


#Dar Bienvinida al usuario
def SaludarUsuario():

    nombre = input('Bienvenido al Recetario Py9, dime como te llamas: ')

    print(f'¡Hola {nombre}. Muchas gracias por usar nuestros servicios')
    print("*" * 100)

def TratamiendoCarpetaRecetario():
    
    #Directorio a escanear 
    directorio_actual = Path('.')
    print(f'Ud se encuentra en la siguiente ruta {directorio_actual.absolute()}')

    #Cantidad de archivos actuales
    contador_archivos = sum(1 for item in directorio_actual.rglob('*.txt') if item.is_file() )
    print(f'Actualmente cuenta con {contador_archivos} recetas')

    print("*" * 100 + '\n')
    
    return directorio_actual

def elegirCategoria(ruta):

    os.system('clear')

    categorias = []
    index = 0

    #Listar Categorias 
    for carpeta in ruta.iterdir() :
        if Path(carpeta).is_dir():
            index += 1
            categorias.append(carpeta)
            print( f'Opción {index} --> categoria: {carpeta}')

    opcion = int(input('\n Seleccione una opción de la lista:'))

    return categorias[opcion - 1]


def ElegirReceta(ruta, categoria):

    os.system('clear')

    recetas = []
    index = 0
    rutaReceta = Path(ruta,categoria)

    #Listar las recetas que tiene la categoria seleccionada
    for receta in rutaReceta.rglob('*.txt'):
        recetas.append(receta.name)
        index += 1
        print(f'Opción {index} --> Receta: {receta.name}')
        
    opcion = int(input('\n Por favor seleccione una receta: '))
    
    return recetas[opcion-1]

def VisualizarReceta(ruta,categoria,receta):

    os.system('clear')

    archivo = Path(ruta,categoria,receta)
    archivo_receta = open(archivo,mode='r')

    print(archivo_receta.readlines())
    
def LeerReceta(ruta):

    os.system('clear')

    categoria = elegirCategoria(ruta)
    print(f'Categoria: "{categoria}" seleccionada')

    receta = ElegirReceta(ruta,categoria)
    print(f'Receta: "{receta}" seleccionada')
    VisualizarReceta(ruta,categoria,receta)

    tecla = input('Presione cualquiera tecla para continuar...')



def EscribirReceta():
    print('Menu Escribir Receta')

    tecla = input('Presione cualquiera tecla para continuar...')
    


# def CrearCategoria():


# def EliminarReceta():


# def EliminarCategoria():


# def Salir():


def ElegirOpcion(ruta,menu):

    salir = 's'
    opcionUsuario = ''

    while opcionUsuario != salir:

        print('*'*20)
        print('Menu Recetas')
        print('*'*20)

        for opcion in menu:
            print(f'Opción {opcion}')

        print('*'*20)
        opcionUsuario = input('Selecciona una opción: ')

        match opcionUsuario:
            case '1':
                LeerReceta(ruta) # 1
                os.system('clear')
            case '2':
                EscribirReceta()
                os.system('clear')

    
    # EscribirReceta() # 2
    # CrearCategoria() # 3  
    # EliminarReceta() # 4 
    # EliminarCategoria() # 5 
    # Salir() # 6 



SaludarUsuario()
ruta = TratamiendoCarpetaRecetario()

ElegirOpcion(ruta,menuRecetas)


    