
dummy_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
texto_prueba = "hola hola mi nombre es jose marques, hola jose marques, mi nombre es karla"
#print(dummy_text.split())

def analiza_texto(lista):
    no_caracteres = 0
    longitud = len(lista)
    misma_palabra = [0] * longitud 
    no_palabras = len(lista)
    for cadena in lista:
        no_caracteres_cadena = len(cadena)
        no_caracteres += no_caracteres_cadena
        
    for j in range(len(lista) - 1):
        for i in range(len(lista) -1):
            if lista[i] == lista[j]:
                misma_palabra[j] += 1 
            else:
                continue 
            
    return no_palabras, no_caracteres, misma_palabra

palabras1, conteo1, misma_palabra1 = analiza_texto(dummy_text.split())
print(palabras1)
print(conteo1)
print(misma_palabra1)


palabras2, conteo2, misma_palabra2 = analiza_texto(texto_prueba.split())
print(palabras2)
print(conteo2)
print(misma_palabra2)