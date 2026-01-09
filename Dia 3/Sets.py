#No puedes incluir ni listas ni dicciones 

mi_set = set((1,2,3,4,5))
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3,3}
print(type(otro_set))

#print(otro_set[0]) no lo soporte y tampoco se puede reescribir 

print(otro_set)

#permite un tupple 
new_set = {9,2,3,(1,2,3)}
print(len(new_set))

print(2 in new_set)


#Union de sets 

union_set = otro_set.union(new_set)
print(union_set)

new_tup = ('ange','cruz')

union_set.add(new_tup)
print(union_set)

sorteo = union_set.pop() 
print(sorteo)

union_set.clear() 
print(union_set)