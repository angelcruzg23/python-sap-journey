

def evaluar_precio(lista_precio):

    precio_mayor = 0 
    nombre_cafe = ''
    
    for cafe,precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_cafe  = cafe
    
    return precio_mayor,nombre_cafe

lista_precio = [('Moka',2.4) , ('Capuccino',1.3), ('Late',2.0), ('Flat White',2.9)]

#tambien puedo almacenar las variables de return de la función en la misma cantidad de variables 

precio,cafe = evaluar_precio(lista_precio)
print(f'El Cafe {cafe} con el precio de {precio} es el mas caro')


#print(evaluar_precio(lista_precio))



