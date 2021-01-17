import os 
import urllib.request

data_dir = 'D:/udemy'

pages =[
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} 
]

for page in pages: 
    try:
        file_name = f'{page["name"]}.html'
        path = os.path.join(data_dir, file_name)

        print(f'Przetwarzanie { page["url"]} ==> {file_name}')
        urllib.request.urlretrieve(page["url"], path)
        print('...zrobione!')
    except:
        print(f'Błąd w przetwarzaniu strony {page["name"]}')
        print('zatrzymanie procesu')
        break

else:
    print('wszystkie procesy zostały przetworzone')