#un programme Python qui  peut vérifier si le premier élément d’une liste est le même que le dernier.
L = [
    5,
    3,
    4,
    7,
    8,
    5
]

print(L[0] == L[-1])

#cette methode permet de faire d'autre chose comme: 
#L'extraction
print(L[0:3]) #du premier element jusqu'a 4eme sans inclure le dernier
print(L[1:])    #du denxieme element jusqu'a la fin
print(L[:5])    #du debut jusqu'a 6eme sans l'inclure
print(L[1:5:2]) #du deuxieme jusqu'a 6eme sans l'inclure avec un pas de 2
print(L[1::2])  #du deuxieme jusqu'a la fin avec un pas de 2
#renverser la liste
print(L[::-1])