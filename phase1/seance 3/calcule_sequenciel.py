#Problème : Calcul de la Somme des Carrés
import time

def SommeCarrés(liste:list):
    carres =[]
    for i in liste:
        carres.append(i**2)
    return sum(carres)



nombres = list(range(1, 1000001))
start_time = time.time()
print(SommeCarrés(nombres))
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time,'s')