#Problème : Calcul de la Somme des Carrés
import time
import multiprocessing

def Carres (liste : list, result: list = []):
    for i in liste:
        result.append(i**2)
    return result
# result = []
result = multiprocessing.Manager().list()
nombres = list(range(1, 1000001))
process1 = multiprocessing.Process(target=Carres, args=[nombres[:len(nombres)//2],result])
process2 = multiprocessing.Process(target=Carres, args=[nombres[len(nombres)//2:],result])
start_time = time.time()
process1.start()
process2.start()
process1.join()
process2.join()
total_somme_carrés = sum(result)
print(total_somme_carrés)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time,'s')