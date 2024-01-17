#Créez une boucle pour calculer la somme des nombres pairs de 1 à 20

#en utilisant for
print('en utilisant for')
for i in range(1,21):
    if i%2 == 0:
        print(i)

#en utilisant for avec pas
print('en utilisant for ave pas')
for i in range(2,21,2):
    print(i)

#en utilisant while
print('en utilisat while')
number = 1
while number <=20:
    if number %2 ==0 :
        print(number)
    number +=1
