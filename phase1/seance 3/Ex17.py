#Utilisez le paradigme fonctionnel pour transformer une liste de nombres en une liste de leurs carrés.
def carre(n:float):
    return n ** 2

nombres = [1, 2, 3, 4, 5]
carres = list(map(carre, nombres))
print(carre)
