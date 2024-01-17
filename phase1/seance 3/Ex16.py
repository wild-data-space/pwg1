#Implémentez un programme en suivant le paradigme procédural pour calculer la somme des éléments d'une liste.
def SommeList(l:list):
    somme = 0
    for element in l:
        somme += element
    return somme
l = [1, 2, 3, 4, 5]
somme = SommeList(l)
print(somme)