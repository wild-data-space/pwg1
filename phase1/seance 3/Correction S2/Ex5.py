#Utilisez une boucle pour afficher les puissances de 2 jusqu'à 64
#en utilisant while sur la base
print('en utilisant while sur la base')
base = 2
while base <= 64:
    print(base)
    base *=2
    
#en utilisant while sur la puissance
print('en utilisant while sur la puissance')
puissance = 1
while True:
    if 2**puissance > 64:
        break
    print(2**puissance)
    puissance +=1

#en utilisant for
print('en utilisant for')
for exposant in range(7): 
    print(2 ** exposant)

#en utilisant for avec bit_length
print('en utilisant for avec bit_length')
puissance_limite = 64
for exposant in range(puissance_limite.bit_length()):
    print(2 ** exposant)

