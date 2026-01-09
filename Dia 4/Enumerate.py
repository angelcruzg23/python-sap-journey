
lista = [1,2,3,4]

#Devuelve un tupple 

for index,item in enumerate(lista):
    index += 1
    print(f"La posición {index} contiene el valor {item}")

#Crear una tupple con base en un tupple
ordenada = list(enumerate(lista))

print(ordenada[1][0])

print(ordenada)
for index,item in ordenada:
    print(index,item)