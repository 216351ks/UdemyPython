listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []

for a in listA:
    for b in listB:
        product.append((a,b))
print(product)

product = {a:b for a in listA for b in listB}
print(product)
