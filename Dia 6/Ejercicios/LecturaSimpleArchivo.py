

mi_archivo = open('Prueba.txt', encoding='latin-1')

# Util para archivo pequeña y se carga todo el archivo, si es muy grande me puedo quedar sin espacio 
# for linea in mi_archivo.readlines():
#     print(f'Aqui Dice {linea.upper()}')

# Es mejor utilizar readline para que vaya linea por linea

abierto = 0 
while abierto == 0:

    linea = mi_archivo.readline()
    if len(linea)==0:
        break
    
    print(f'Aqui Dice {linea}')
    
# una_linea = mi_archivo.readline()
# print(una_linea)

# una_linea = mi_archivo.readline()
# print(una_linea.rstrip())

# una_linea = mi_archivo.readline()
# print(una_linea)

mi_archivo.close() 

