
def alfa_sorter(palabra):

    palabra = list(set(palabra))
    palabra.sort()
    return palabra


print(alfa_sorter('entretenido'))
