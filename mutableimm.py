number = 10
print('variable number:', number, id(number))

number += 2
print('variable number:', number, id(number))

txt = 'Afrika'
print('variable text:', txt , id(txt))

txt += ' is hot'
print('variable text:', txt , id(txt))

'''
mutable = zmienny
immutable=niezmienny
'''
'''
string=immutable
'''

lista = [1,2,3]
print('variable list:', lista, id(lista))
lista.append(4)
print('variable list:', lista, id(lista))

'''
mutable=zmienny (lista)
'''

lista2 = lista 
print('variable list:', lista2, id(lista2))
lista2.append(5)
print('variable list:', lista, id(lista))
print('variable list:', lista2, id(lista2))

lista3= lista.copy()
print('variable list:', lista, id(lista))
print('variable list:', lista3, id(lista3))
lista3.append(5)
print('variable list:', lista, id(lista))
print('variable list:', lista3, id(lista3))
