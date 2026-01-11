
def validar_cero_repetido(*numeros):

    last_number = ''
    for n in numeros:
        if n==0 and last_number==0:
            return True
        else:
            last_number=n
    

    return False


print(validar_cero_repetido(5,6,1,0,0,9,3,5))
print(validar_cero_repetido(6,0,5,1,0,3,0,1))