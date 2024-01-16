#un programme qui classe trois nombres dans l'ordre croissant.
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))
nombre3 = int(input("Entrez le troisième nombre : "))

if nombre1 <= nombre2 and nombre1 <= nombre3:
    if nombre2 <= nombre3:
        nombres_triés = [nombre1, nombre2, nombre3]
    else:
        nombres_triés = [nombre1, nombre3, nombre2]
elif nombre2 <= nombre1 and nombre2 <= nombre3:
    if nombre1 <= nombre3:
        nombres_triés = [nombre2, nombre1, nombre3]
    else:
        nombres_triés = [nombre2, nombre3, nombre1]
else:
    if nombre1 <= nombre2:
        nombres_triés = [nombre3, nombre1, nombre2]
    else:
        nombres_triés = [nombre3, nombre2, nombre1]
print("Les nombres triés dans l'ordre croissant sont :", nombres_triés)

#mehode 2
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))
nombre3 = int(input("Entrez le troisième nombre : "))

nombres = [nombre1, nombre2, nombre3]
nombres.sort()

print("Les nombres triés dans l'ordre croissant sont :", nombres)

