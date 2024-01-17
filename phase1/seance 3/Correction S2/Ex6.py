#Utilisez une boucle pour trouver le plus petit carré parfait supérieur à 100.
#un carre parfait est un carre d'un nombre entier positif
#en utilisant while avec racine carre
print('en utilisant while')
from math import sqrt
number = 101
while True:
    if sqrt(number).is_integer():
        print(number)
        break
    number +=1

#en utilisant for
print('en utilisant for')
for i in range(100):
    if i**2 > 100:
        print(i**2)
        break