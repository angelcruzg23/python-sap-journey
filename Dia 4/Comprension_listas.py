palabra = 'python'

#Letra por cada Letra. es como que primero creo una variable para recibir el valor de cada registro 
#que se encuentra en el array de palabras 
lista = [letra for letra in palabra]

print(lista)

lista = [n for n in range(1,50)]
print(lista) 

#Con condicionales 
lista = [n for n in range(1,50) if n%2==0 ]
print(lista) 

lista = [n if n%2==0 else n>20 for n in range(1,50) ]
print(lista) 

pies = [10,20,30,40,50]

conversion_pies = 3.281

metros = [p * conversion_pies for p in pies]
print(metros)