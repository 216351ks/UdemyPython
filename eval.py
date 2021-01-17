var_x = 10
password = 'Super secret passwd'


source = '__import__("os").getcwd()'

#globals = globals().copy()
#del globals['password']
globals = {}


result = eval(source, globals)
print(result)

#print(globals())