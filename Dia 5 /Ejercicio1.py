
def devolver_distintos(n1,n2,n3):

    numeros = [n1,n2,n3]
    numeros.sort()
    suma = sum(numeros)

    if suma > 15:
        return max(numeros)
    elif suma < 10:
        return min(numeros)
    else:
        return numeros[1]

print(devolver_distintos(3,2,3))