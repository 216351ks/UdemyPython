def DisplayOptions(opcje):

    for z in range(len(opcje)):
        print(f'{z+1} - {opcje[z]}')

    wybor = input('Select option above or press enter to exit: ')
    return wybor

wybor ='x'
opcje=['load data', 'export data', 'analyze & predict']

while wybor: 

    wybor = DisplayOptions(opcje)

    if wybor:
        try:
            wybor_num = int(wybor)-1
            if wybor_num >=0 and wybor_num<len(opcje):
                print(f'wybrałeś {wybor_num + 1} - {opcje[wybor_num]}')
            else:
                print("wybierz wartość z listy")
        except:
            print("wprowadz cyfrę!")
    else: 
        print("koniec")
