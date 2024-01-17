#Utilisez une boucle pour afficher les carrés des nombres de 1 à 5
#en utilisant for
print('en utilisant for')
for element in range(1,6):
    print(element**2)

#en utilisant les listes comprehensive
print('en utilisant liste comprehensive')
numbers = [i**2 for i in range(1,6)]
print(numbers)

#en utilisant while
print('en utilisant while')
number = 1
while number <=6:
    print(number **2)
    number +=1

#en utilisant while avec break
print('en utilisant while avec break')
number = 1
while True:
    print(number **2)
    number +=1
    if number > 6:
        break