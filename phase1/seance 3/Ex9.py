#Écrivez une fonction pour vérifier si un nombre est premier.
def EstPremier(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(EstPremier('10'))