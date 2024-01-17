#Écrivez une fonction pour calculer la somme des chiffres d'un nombre.
def SommeNombre(n:int):
    n = str(n)
    result = 0
    for i in n:
        result += int(i)
    return result


#par un autre paradigme
def SommeNombre(n:int):
    l = [int(i) for i in str(n)]
    return sum(l)