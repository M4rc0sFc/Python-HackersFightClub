
#Funciona solo para cadenas que sean palindromos que no sean espacios
def es_palindromo(cadena):
    lista1 = list(cadena)
    lista2 = lista1[::-1]
    if lista1 == lista2:
        return True 
    else:
        return False
    
    
print(es_palindromo('anilina'))
print(es_palindromo('anilina s'))