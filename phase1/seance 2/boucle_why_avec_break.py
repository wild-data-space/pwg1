#Essayons de refaire la même chose mais pour un ensemble de nombre donnés par l’utilisateur jusqu’a ce qu’il écrit N
while True:
    a = input('Donnez un nombre: ')
    if a == 'N':
        break
    else:
        a = int(a)
        if a % 5 == 0 and a % 3 ==0:
            print(a,'est divisible par 5 et 3')
        else:
            print(a,"n'est pas divisible par 5 ni 3")