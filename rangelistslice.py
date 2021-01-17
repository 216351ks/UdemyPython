for i in range(1,10,2): '''printuje od 1 do 10 co 2'''
    print(i)

for x in range(10,0,-1): '''printuje od 10 do 1'''
    print(x)

lista = lista(range(20))
print('Lista: ', lista, type(lista))

lista2= lista.copy()
print('Lista: ', lista2, type(lista2), id(lista2))

print(lista[5:7]) '''print od 5 do 7'''

print(lista[5:]) '''printuje od 5 do końca'''

print(lista[:-1]) '''printuje wszystko do przedostatniego'''

print(lista[-1:0:-1]) '''od 9 do 1 do 1'''

print(lista[::-1]) '''printuje od końca'''
