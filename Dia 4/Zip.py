nombres = ['Luis','Pedro','Maria']
edades  = [19,30,99]
ciudades = ['Lima','Caracas','Madrid']

personas = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in personas:
    print(f"{nombre} tiene {edad} años de edad y vive en {ciudad}")