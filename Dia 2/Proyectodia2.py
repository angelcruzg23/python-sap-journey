
## Calculo de comisiones de ventas 

## Pregunto el nombre del vendedor 
nombre_vendedor = input("Hola representante de ventas, ¿Cual es tu nombre? -> ")

##Luego pregunto cuanto vendió
ventas = input(f"Estimado/a {nombre_vendedor}, ¿Cuales fueron tus ventas mensuales? -> ")

##Calcular comision
comision = 0.13
valor_comision = float(ventas) * comision

##Informar del valor de la comisión generada
print(f"Estimado/a {nombre_vendedor} su comisión por las ventas de {ventas} es de: ${round(valor_comision,2)}  \n ¡Muchas Gracias!")
