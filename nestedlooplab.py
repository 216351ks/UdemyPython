ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

lot = []
lot2 = []

for start in ports:
    for stop in ports:
        if start !=stop:
            lot.append((start,stop))
print(lot)
print(len(lot))
print("-"*20)

for a in ports:
    for b in ports:
        if a<b:
            lot2.append((a,b))

print(lot2)
print(len(lot2))
