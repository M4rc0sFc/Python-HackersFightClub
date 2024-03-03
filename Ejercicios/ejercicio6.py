#!/usr/bin/python
#HACKERS_FIGHT_CLUB

simpsons = ['homero','lisa','bart']
pokemon = ['ash','brock','misty']
rickymorty = ['rick','morty','jerry','squanchy']
malcom = ['dewey','reese','hal','lois','francis','malcom']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION

def a_mayuscula(lista):
    return lista.upper()

suma_listas = lambda lista1, lista2, lista3, lista4: lista1 + lista2 + lista3 + lista4 
lista_resultante = suma_listas(simpsons,pokemon,rickymorty,malcom)
lista_filtrada = [cadena for cadena in lista_resultante if 'i' in cadena]
lista_filtrada_MAYUSCULAS = map(a_mayuscula, lista_filtrada)
print(suma_listas(simpsons,pokemon,rickymorty,malcom))
print(list(lista_filtrada_MAYUSCULAS))