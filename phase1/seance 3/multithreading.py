#Problème : Calcul de la Somme des Carrés
import time
import threading

def Carres (liste : list, result: list = []):
    for i in liste:
        result.append(i**2)
    return result
result = []
nombres = list(range(1, 1000001))
thread1 = threading.Thread(target=Carres, args=[nombres[:len(nombres)//2],result])
thread2 = threading.Thread(target=Carres, args=[nombres[len(nombres)//2:],result])
start_time = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
total_somme_carrés = sum(result)
print(total_somme_carrés)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time,'s')