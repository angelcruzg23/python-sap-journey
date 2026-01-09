
#Mensaje del usuario 
cadena = input("Ingrese una cadena de texto: ")

cadena = cadena.lower()

#¿Cuantas veces aparece cada letra que el usuario ingresa? 
letra_key = input('Introduzca las 3 letras que desea buscar cuantas veces se repite -> ')
lista_letra_key = list(letra_key)

lista_letras = list(cadena)
print(f"Caso #1 La cantidad de veces que aparece la letra '{lista_letra_key[0]}' es de -> {lista_letras.count(lista_letra_key[0])} veces")
print(f"Caso #1 La cantidad de veces que aparece la letra '{lista_letra_key[1]}' es de -> {lista_letras.count(lista_letra_key[1])} veces")
print(f"Caso #1 La cantidad de veces que aparece la letra '{lista_letra_key[2]}' es de -> {lista_letras.count(lista_letra_key[2])} veces")

#Cantidad de palabras que hay en la frase 
lista_palabras = cadena.split()
print(f"Caso #2 La cantida de palabras que hay en el texto es de -> {len(lista_palabras)}")

#Cual es la primera y última letra del texto 
print(f"Caso #3 La primera letra del texto es {lista_letras[0]} y la última lentra es {lista_letras[len(lista_letras) -1]}")

#Texto invertido
print(f"Caso #4 El texto invertido se vería de la siguiente forma {cadena[::-1]}")
lista_palabras.reverse()
texto_invertido = " ".join(lista_palabras)
print(f"Caso #4 El texto invertido se vería de la siguiente forma {texto_invertido}")


#Validar si la palabra python se encuentra 
validar_python = 'python' in cadena
dicSiNo = {True:'si', False:'no'}

print(f"Caso #5 Validar si la palabra python se encuentra en la cadea {'python' in cadena} ")
print(f"Caso #5 La palabra 'python' {dicSiNo[validar_python]} se encuentra en el texto")

