import math

multiply = lambda x,y,z: x*y*z
is_empty = lambda lista:len(lista) == 0
has_n_elements = lambda lista,n: len(lista) == n 
sqrt = lambda num: math.sqrt(num)
interseccion = lambda conj1,conj2: conj1.intersection(conj2) 


lista1_prueba = []
lista2_prueba = [1,2,3,4,5]
conjunto1_prueba = {1,2,3,4}
conjunto2_prueba = {2,3,4}


print(multiply(2,3,4))
print(is_empty(lista1_prueba))
print(has_n_elements(lista2_prueba, 5))
print(sqrt(25))
print(interseccion(conjunto1_prueba, conjunto2_prueba))