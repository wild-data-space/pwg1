#Utilisez une boucle pour trouver la moyenne de nombres saisis par l'utilisateur jusqu'à ce qu'il entre -1

#en utilisant while
nombres = []
while True:
    a = int(input('Donnez un nombre: '))
    if a == -1:
        print(sum(nombres)/len(nombres))
        break
    nombres.append(a)
