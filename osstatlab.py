import os 

def plik(path): 
    with open(path,'r') as f: 
        plik_txt=f.read()

        plik_words= len(plik_txt.split())
        return plik_words

path= r'D:\udemy\pliktestowy.txt'

if os.path.isfile(path):
    print(f'w {path} jest {plik(path)} słów')

os.path.isfile(path) and print(f'w {path} jest {plik(path)} słów')
