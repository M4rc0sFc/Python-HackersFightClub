
import string 
import random 

def genera_contrasena_aleatoria(minusculas,mayusculas,digitos,contrasena = ""):
    
    #Caso Base 
    if minusculas == 0 and mayusculas == 0 and digitos == 0:
        return contrasena 

    #Caso recursivo    
    #Siguiente caracter a elegir
    eleccion = []
    if minusculas > 0:
        eleccion.append('m')
    if mayusculas > 0:
        eleccion.append('M')
    if digitos > 0:
        eleccion.append('d')
        
    caracter_elegido = random.choice(eleccion)
    
    match caracter_elegido:
        case 'm':
            return genera_contrasena_aleatoria(minusculas - 1, mayusculas, digitos, contrasena + random.choice(string.ascii_lowercase))
        case 'M':
            return genera_contrasena_aleatoria(minusculas, mayusculas - 1, digitos, contrasena + random.choice(string.ascii_uppercase))
        case 'd':
            return genera_contrasena_aleatoria(minusculas, mayusculas, digitos - 1, contrasena + random.choice(string.digits))
        

nueva_contrasena = genera_contrasena_aleatoria(3,4,6)
print(nueva_contrasena)