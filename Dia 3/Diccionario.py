# diccionario = {
#     "Nombre" : "Angel",
#     "Apellido" : "Angel"
# }
# print(type(diccionario))
# print(diccionario["Nombre"])


# dic = {
#     'c1' : 55,
#     'c2' : [
#         10,
#         20,
#         30
#     ],
#     'c3' : {
#         's1' : 100,
#         's2' : 200
#     }
# }

# print(dic['c3']['s1'])

# dic1 = {
#     'c1': [
#         'a','b','c'
#     ],
#     'c2' : [
#         'd','e','f'
#     ]
# }

# letra = dic1['c2'][1].upper()
# print(dic1['c2'][1].upper())

dic = {
    1 : 'a',
    2 : 'b'
}

dic[3] = 'c'

print(dic)


dic[2] = 'x'

print(dic)

print(dic.keys())
print(dic.values())
print(dic.items()) # Lo que regresa es un tupples

