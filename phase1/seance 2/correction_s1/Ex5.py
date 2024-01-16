#Un programme qui vérifie si un nombre est divisible par 5 et 3.

a = int(input('Donnez un nombre a: '))
if a % 5 == 0 and a % 3 == 0:
    print(a,'est divisble par 5 et 3')
elif a % 5 == 0:
    print(a,'est divisible par 5')
elif a % 3 == 0 :
    print(a,'est divisible par 3')
else:
    print(a,'n\'est divisible ni par 5 ni 3')