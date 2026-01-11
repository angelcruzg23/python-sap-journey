def reducir_lista(lista_numeros):
    
    lista_numeros = list(set(lista_numeros))
    lista_numeros.sort()
    lista_numeros.pop(-1)
    
    return lista_numeros
    
def promedio(lista_numeros):
    
    promedio = sum(lista_numeros) / len(lista_numeros)
    return promedio
    

lista = reducir_lista([1,2,15,7,2,8])
print(promedio(lista))
