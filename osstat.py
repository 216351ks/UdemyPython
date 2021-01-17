import os 

path = r'D:\udemy\data.txt'

#os.remove(path)

'''
if os.path.isfile(path):
    print("file %s exist" % path)

else: 
    print('creating a file %s' % path)
    open(path, 'x').close()
    print('file %s created' % path)
'''

result =os.path.isfile(path) or open(path, 'x').close()
print(result)