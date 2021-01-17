import datetime as dt

price = 123
bonus = 23
bonus_granted = True

price = price - bonus if bonus_granted else price
print(price)

print('-------------------------------------')

rating =5 

print('very good' if rating ==5 else 'good' if rating ==4 else 'weak')

print('-------------------------------------')


today = dt.date.today().strftime("%A")

if today == 'Monday':
    print('nauka')
elif today == 'Tuesday':
    print('gotowanie')
elif today == 'Wednesday':
    print('programowanie')
elif today == 'Thursday':
    print('spanie')
elif today == 'Friday':
    print('sprzątanie')
elif today == 'Saturday':
    print('studia')
else:
    print('studia i nauka')    
