#Est ce que c’est possible de refaire l’exercice 5, mais cette fois sur tous le nombres entre 10 et 30 
for a in range (10,31):
    if a % 5 == 0 and a % 3 == 0:
        print(a,'est divisble par 5 et 3')
    elif a % 5 == 0:
        print(a,'est divisible par 5')
    elif a % 3 == 0 :
        print(a,'est divisible par 3')
    else:
        print(a,'n\'est divisible ni par 5 ni 3')