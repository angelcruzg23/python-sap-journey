
def suma(*args):

    total = 0 

    for arg in args:
        total += arg
    
    return total


print(suma(1,2,3,4,1000))