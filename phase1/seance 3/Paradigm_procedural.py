def divisible (n: int):
    if a % 5 == 0 and a % 3:
        return True
    elif a % 5 == 0:
        return 5
    elif a % 3 == 0:
        return 3
    else:
        return False
    
while True:
    a = input('Donnez un nombre: ')
    if a.upper() == 'N':
        break
    try:
        a = int(a)
        print(divisible(a))
    except:
        print('valeur non numerique')
    