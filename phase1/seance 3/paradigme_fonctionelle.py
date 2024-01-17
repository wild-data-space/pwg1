divisible3 = lambda x: x % 3 == 0
divisible5 = lambda x: x % 5 == 0
divisible = lambda x : divisible3(x) and divisible5(x)
def validite (n:str):
    try:
        n = int(n)
        return n
    except:
        print('None numerique')
        return 1
while True:
    a = input('Donnez un nombre')
    if a.upper() == 'N':
        break
    print(divisible(validite(a)))
