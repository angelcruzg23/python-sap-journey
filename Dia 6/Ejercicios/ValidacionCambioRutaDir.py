import os 

ruta = os.chdir('archivos/')

archivo = open('prueba.txt',mode='r',encoding='latin-1')
print(archivo.read())
archivo.close() 
