
##Repeticicón de definida de N veces 

#Por cada elemento en nombres
    #Imprimir ("hola")

nombres = ['Juan','Maria','Pedro']
for nombre in nombres:
    posicion = nombres.index(nombre) + 1 # Los indices comienzan en la posición 0 
    print(f"Hola {nombre} en la posición {posicion}")

    #Puedo implemntar control de flujo 
    if nombre.startswith('J'):
        print("Nombre comienza con J")

print('Fin de programa')

palabra = 'Python'

for letra in palabra:
    print(letra)

#Tambien puede existir el valor dentro de la repetición
for letra in 'palabra':
    print(letra)

#Tambien pueden ser listas dentro de listas 
for obj,x in [[1,2],[2,3],[1,3]]:
    print(obj,x)

#Diccionarios 
ventas_mes = {
    "Enero":100,
    "Febero" : 200,
    "Marzo" : 300
}

#Primera versión
for mes in ventas_mes:
    print(f"La venta para el mes de {mes} es de {ventas_mes[mes]}")

#Segunda versión manejando Items 
for mes,valor in ventas_mes.items():
    print(f"La venta para el mes de {mes} es de ${valor}")

#Tercera versión solo manejando valores 
for valor in ventas_mes.values():
    print(f"La venta para el mes es de ${valor}")

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for n in lista_numeros:
    suma_numeros = suma_numeros + n


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for n in lista_numeros:
    if n%2==0: #Numero par 
        suma_pares = suma_pares + n
        
    else:
        suma_impares = suma_impares + n

