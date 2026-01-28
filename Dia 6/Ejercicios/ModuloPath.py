
#No es un metodo es un objeto por eso va en Mayuscula
from pathlib import Path

# carpeta = Path('archivos')

# archivo = carpeta / 'prueba.txt'

# datos = open(archivo)

# print(datos.readline())

# print(carpeta.stem)
# print(archivo)

# carpeta = Path('archivos1')
# if not carpeta.exists():
#     print('No existe la carpeta')


#Creacion de rutas de directorios 

#Para tener la ruta absoluta utilizar el metodo Home 
base = Path.home()
print(base)

#Tiene una ruta relativa 
guia = Path("Barcelona", "Sagrada Familia.txt")
print(guia)

#Si conbino las dos instancia 
mix = Path(base,'Barcelona','Sagrada Familia.txt')
print(mix)

#Puedo incluir objetos dentro Path
mix_objects = Path(base,"Europa","España", Path("Barcelona","Sagrada Familia.txt"))
print(mix_objects)

#Puedo reutilizar la ruta que ya he creado antes agregar un nuevo archivo 
mix_objects2 = mix_objects.with_name('La Pedrera.txt')
print(mix_objects2)

#Devolver el antecesor de parten
print(mix_objects.parent) #-> puedo ir con más parent 

#Enumerara archivos del Path
enumerar_archivos = Path(Path.home(),"Europa")

#Listar cada archivos 
for txt in Path(enumerar_archivos).glob('*.txt'):
    print(txt)

#Listar todos los archivos en todas las carpetas
for txt in Path(enumerar_archivos).glob('**/*.txt'):
    print(txt)




