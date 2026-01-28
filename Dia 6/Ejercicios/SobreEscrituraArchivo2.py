
# Modo apertura R = ReadOnly 
# Modo apertura W = Solo Escritura lo resetea y lo crea  
# Modo sobre escritura A = Sobrescribe el archivo 

mi_archivo = open('Prueba.txt',encoding='latin-1',mode='a')
mi_archivo.write('Soy la nueva linea \n')
mi_archivo.close() 


mi_archivo = open('Prueba.txt',encoding='latin-1')
print(mi_archivo.readlines())
mi_archivo.close() 

mi_archivo = open('Prueba.txt',encoding='latin-1',mode='a')
mi_archivo.write('''
Soy la nueva linea de otra manera 
''')
mi_archivo.close() 

lista = ['Hola\n','Mundo\n']
mi_archivo = open('Prueba.txt',encoding='latin-1',mode='a')
mi_archivo.writelines(lista)
mi_archivo.close() 


lista = ['Hola 2 \n','Mundo 2 \n']
mi_archivo = open('Prueba.txt',encoding='latin-1',mode='a')

for l in lista:
    mi_archivo.write(l + '\n')

mi_archivo.close() 
    

mi_archivo = open('Prueba.txt',encoding='latin-1',mode='r')
for linea in mi_archivo.readlines():
    print(linea)



