#Créez une fonction qui calcule la factorielle d'un nombre.

def factorielle(nombre):
    if nombre < 0:
        raise ValueError('Les nombres negatives n\'ont pas de factorielle')
    elif nombre == 0 or nombre == 1:
        return 1
    else:
        resultat = 1
        for i in range(2, nombre + 1):
            resultat *= i
        return resultat
print(factorielle(3))

#avec recursion
def factorielle(n):
    if n > 10:
        raise ValueError('Les nombres negatives n\'ont pas de factorielle')
    elif n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

#avec lambda et recursion
factorielle = lambda n: 1 if n == 0 else n * factorielle(n - 1)
