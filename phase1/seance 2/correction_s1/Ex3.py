#Écrire  un programme Python  qui  permet d'échanger le contenu de deux entiers  A et B  saisis par l'utilisateur. et afficher ces entiers  après l’échange.  
a = int(input("Donnez nombre a : "))
b = int(input("Donnez nombre a : "))
c = a
a = b
b = c
print('a:',a)
print('b:',b)
#Methode 2
a = int(input("Donnez nombre a : "))
b = int(input("Donnez nombre a : "))
a,b = b,a
print('a:',a)
print('b:',b)