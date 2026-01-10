
serie = 'N-3'

match serie:
    case 'N-01':
        print("Samsung")
    case 'N-02':
        print("Apple")
    case _:
        print("No hay concidencia")

#Utilidad para detectar patrones con match 
cliente = {
    'nombre':'Angel',
    'edad':45,
    'ocupacion':'Developer'
}

pelicula = {
    'titulo':'Matrix',
    'ficha_tecnica' : {
        'protagonista':'Keaune Reeve',
        'director':"Lana y Llly Wanososky"
    }
}

elementos = [cliente,pelicula,'libros']

#Iteramos la lista de elementos porque si la mandamos a imprimir, que sale? 
print(elementos )

for e in elementos:
    match e:
        case {
            'nombre':nombre,
            'edad':edad,
            'ocupacion':ocupacion
            }:
            print(nombre,edad,ocupacion)
        case {
            'titulo':titulo,
            'ficha_tecnica': {
                'protagonista':protagonista,
                'director':director
                }
            }:
            print(titulo,protagonista,director)
        case _:
            print('No se que es esto')