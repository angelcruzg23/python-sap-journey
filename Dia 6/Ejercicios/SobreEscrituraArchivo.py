registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
mi_archivo = open('registro.txt',mode='w')
mi_archivo.writelines('\t'.join(registro_ultima_sesion) + '\n')
mi_archivo.close()

mi_archivo = open('registro.txt',mode='r')
for linea in mi_archivo.readlines():
    print(linea)
mi_archivo.close()