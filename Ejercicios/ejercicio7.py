#Las llaves del diccionario serán los números odiosos menores a 50 

llaves = [1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26, 28, 31, 32, 35, 37, 38, 41, 42, 44, 47, 49]

#Creacion del diccionario
# usamos las funciones bin() y hex() de Python para obtener la representación en binario y en haxadecimal del número odioso que representa la llave en nuestro diccionario
diccionario = {key: (bin(key)[2:], hex(key)[2:]) for key in llaves}

#Impresión del diccionario 
for k, v in diccionario.items():
    print(f"{k}: {v}")