def suma(**kwargs):

    for a,b in kwargs.items():
        print(a,b)


suma(a=1,b=2,c=3)


def prueba(n1,n2,*args,**kwargs):

    print(n1)
    print(n2)

    for n in args:
        print(n) 
    

    for a,b in kwargs.items():
        print(a,b)


prueba(1,2,100,300,400,c=1,b='dos',x=2.9)

#Probando otro metodo de enviar args y kwargs 
lista = [1,3,4,100]

diccionario = {'Nombre':'Angel','Apellido':'Cruz'}

prueba(100,200,lista,diccionario)

def describir_persona(nombre,**caracteristicas):
    
    print(f'Características de {nombre}')
    
    for caracterisitica,valor in caracteristicas.items():
        print(f'{caracterisitica}: {valor}')


caracteristicas = {
    'Color Ojos':'Marron',
    'Color Cabello':'Negro'
}

nombre = 'Angel'


describir_persona("María", color_ojos="azules", color_pelo="rubio")

