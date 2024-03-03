
from math import isqrt 


def es_palindromo(cadena):
    lista1 = list(cadena)
    lista2 = lista1[::-1]
    if lista1 == lista2:
        return cadena  
    else:
        return 'la palabra no es un palindromo'


def es_primo(n: int):
    if n <= 3:
        return n >= 1 
    if n % 2 == 0 or n % 3 == 0:
        return False 
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
 

def esPrimo(n,i):
    lista_primos = []
     #Caso base
    if (n <= 2):
        lista_primos.append(n)
        return True
    if (n % i == 0):
        return False
    if (i * i > n):
        lista_primos.append(n)
        return True 
    
    # Proximo divisordivisor
    return isPrime(n, i + 1)
    
    
