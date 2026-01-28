
import os 

ruta = 'archivos/prueba.txt'

elementoArchivo = os.path.basename(ruta)
print(f'El archivo del directorio seleccionado es: {elementoArchivo}') 

elementoDirectorio = os.path.dirname(ruta)
print(f'El directorio seleccionado es: /{elementoDirectorio}')

rutaCompleta = os.path.split(ruta)
print(f'La ruta completa del directorio es: {rutaCompleta}')

os.rmdir('archivos/remover')



