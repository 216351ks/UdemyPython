workDays = [19,20,21,22,23]

print(workDays)

enumerateworkDays = list(enumerate(workDays))

print(enumerateworkDays)

for pos,value in enumerateworkDays:
    print(f'Pozycja: {pos}, Wartość: {value}')

mies = ['I', 'II', 'III', 'IV', 'V','VI']

miesDays = list(zip(mies,workDays))

print(miesDays)

for m,d in miesDays:
    print(f'Month: {m}, Dni: {d}')

for pos, (m,d) in enumerate(zip(mies, workDays)):
    print(f'Pozycja: {pos} , miesiąc: {m}, dzień: {d}')