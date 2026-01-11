
# def chequar_3_cifras(lista):
    
#     for n in lista:
#         if n in range(100,1000):
#             return True
#         else:
#             pass

# print(chequar_3_cifras([1,3,100]))

def chequear_3_cifras(lista):

    lista_salida = []

    for n in lista:
        if n in range(100,1000):
            lista_salida.append(n)
    
    return lista_salida

print(chequear_3_cifras([1,200,4,98,999,65,456]))
