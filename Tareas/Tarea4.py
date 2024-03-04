#Script para dar un número aleatorio y pedir al usuario que adivine el número hasta que lo logre.
import random 


def revuelve_lista(lista):
    for i in range(len(lista) - 1, 0, -1):
        j = random.randint(0, i)  
        lista[i], lista[j] = lista[j], lista[i]
    return lista


def comparacion(n,m):
    if n < m or n > m:
        return False
    else:
        return True

lista_prueba = [i for i in range(99)]

lista_revuelta = revuelve_lista(lista_prueba)
print(lista_revuelta[41])

numero_adivinado = int(input("Adivina el número: "))

while True:
    if comparacion(lista_revuelta[41], numero_adivinado):
        print("Haz adivinado el número correcto")
        break 
    else:
        numero_adivinado = int(input("Adivina el número: "))
        
    