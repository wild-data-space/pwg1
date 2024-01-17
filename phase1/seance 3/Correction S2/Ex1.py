#Écrivez une boucle qui affiche les nombres de 1 à 10
#En utilisant for
print('En utilisant for')
for nummber in range(1,11): #cette ligne declare une boucle for traduit comme: pour chque nombre dans l'intervale entre 1 et 11 sans l'inclure
    print(nummber)

#En utilisant while
print('en utilisant while')
nummber = 1 #on doit declarer le nombre d'initiation 1
while nummber <=10: #on declare la boucle par condition de repetition: Tant que le nombre est inferieur ou egale a 10
    print(nummber)
    nummber +=1 #on incremente le nombre par 1 pour passer a la deuxieme iteration

#en utilisant while avec break
print('en utilisant while avec break')
number = 1
while True:
    print (number)
    number +=1
    if number >10:
        break