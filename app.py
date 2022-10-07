import sys, random

def menu():
    print('Password Generator v1.4')
    print('1) Start\n2) Exit')
    option = input('Select Option: ')
    if option == '1':
        app()
    elif option == '2':
        sys.exit()
    else:
        print('\ntry again.')
        menu()
        
        
def app():
    pass_length = int(input('Password length: '))

    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '0','1','2','3','4','5','6','7','8','9','!','#','$',
        '%','&','(',')','*','+',',','/',':',';','<','=','>',
        '?','[',']','~','`','^','\\','_','-','{','}','.']
    passw = ''
    for x in range(pass_length):
        tmp = chars[random.randint(0,len(chars)-1)]
        passw = str(tmp) + str(passw)
    print('\n'+passw+'\n')
    menu()



if __name__ == '__main__':
    menu()
