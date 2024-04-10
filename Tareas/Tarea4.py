#función para generar numeros aleatorios
def pseudo_random_number(i):
    user_input = input("Please type anything and press Enter: ")

    ascii_sum = sum(ord(c) for c in user_input)

    random_numbers = []

    for j in range(i + 1):  
        pseudo_random = (ascii_sum * (j + 1)) % (i + 1)  # Example mathematical operation

        random_numbers.append(pseudo_random)  

    return random_numbers


def comparacion(n,m):
    if n < m or n > m:
        return False
    else:
        return True

lista_prueba = pseudo_random_number(99)
#Imprime la lista generada y el número seleccionado a adivinar.
#print(lista_prueba)
#print(lista_prueba[41])
print(lista_prueba[41])

numero_adivinado = int(input("Adivina el número: "))

while True:
    if comparacion(lista_prueba[41], numero_adivinado):
        print("Haz adivinado el número correcto")
        break 
    else:
        numero_adivinado = int(input("Adivina el número: "))
