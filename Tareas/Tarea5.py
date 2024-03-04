
import string 
import random 

# La lista indicativa nos inidica que tipo de información le estamos pidiendo al usuario
lista_indicativa = ['Nombre', 'Nombre mascota', 'Color', 'Estacion', 'Edad', 'Sabor de helado', 'Comida', 'Signo zodiacal', 'Dia de la semana favorito', 'Mes favorito']
lista_prueba = ['Juan', 'Manchas', 'Rojo', 'Primavera', '25', 'Chocolate', 'Pizza', 'Aries', 'Viernes', 'Julio']


def convert_to_uppercase(cadena):
    resultado = ""
    for i in range(len(cadena)):
        if i % 2 == 0:
            resultado += cadena[i].upper()
        else:
            resultado += cadena[i]
    return resultado



def convert_to_lowercase(cadena):
    resultado = ""
    for i in range(len(cadena)):
        if i % 2 == 0:
            resultado += cadena[i].lower()
        else:
            resultado += cadena[i]
    return resultado


def convertir_letras_a_numeros(cadena):
  """
  Convierte las letras de una cadena a números según la siguiente regla:
  a -> 1, b -> 2, ..., z -> 26
  Parámetros:
    cadena (str): La cadena que se desea convertir.

  Retorna:
    str: La cadena con las letras convertidas a números.
  """
  letras = "abcdefghijklmnopqrstuvwxyz"
  numeros = "12345678901234567890123456"
  tabla_conversion = dict(zip(letras, numeros))
  resultado = ""
  for caracter in cadena.lower():
    if caracter in tabla_conversion:
      resultado += tabla_conversion[caracter]
    else:
      resultado += caracter
  return resultado


def switch_case(cadena, numero):
  if numero == 1:
    return convert_to_uppercase(cadena)
  elif numero == 2:
    return convert_to_lowercase(cadena)
  elif numero == 3:
    return convertir_letras_a_numeros(cadena)
  else:
    return "Opción por defecto"

elementos_de_contrasena = []

for i in range(len(lista_prueba)):
  if i % 3  == 0:
    j = 3
  elif i % 2 ==  0:
    j = 2
  else:
    j = 1   
  
  elementos_de_contrasena.append(switch_case(lista_prueba[i],j))    


contrasena_final = ""
for cadena in elementos_de_contrasena:
  contrasena_final += cadena 
print(contrasena_final)