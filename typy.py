myvar = "hello pycharm!"
myvar2 = myvar + "!!"
print(myvar,myvar2)
print(type(myvar), type(myvar2))
print('is value the same:', myvar==myvar2)
print('are the values the same:', myvar is myvar2)
print(id(myvar), id(myvar2))

myvar2 = myvar2[:-2]
print(myvar,myvar2)
print(type(myvar), type(myvar2))
print('is value the same:', myvar==myvar2)
print('are the values the same:', myvar is myvar2)
print(id(myvar), id(myvar2))