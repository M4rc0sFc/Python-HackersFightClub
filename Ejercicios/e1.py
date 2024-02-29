#!/usr/bin/python
#HACKERS_FIGHT_CLUB

aprobados = []

def aprueba_alumno(nombre_completo):
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        if n in ['Diego', 'Alan', 'Guadalupe', 'Rafael', 'Marco']:
            return False
    aprobados.append(nombre_completo.upper())
    return True

def borra_alumno(nombre_completo):
    if nombre_completo.upper() in aprobados:
        aprobados.remove(nombre_completo.upper())
        return True
    else: 
        return False

alumnos = [
    'Abaustista Erick',
    'Anaya Pérez Ulises Josué',
    'Bautista Parra Jonathan',
    'Castro Rendón Diego',
    'Castro Sierra Etni Sarai',
    'Chavez Bolaños Gustavo',
    'Cornejo de la Mora Iñaki',
    'Cruz Hérnandez Víctor Emiliano',
    'Flores Cid Marco',
    'García Chavelas Jonás',
    'García Rosas Dicter Tadeo',
    'García Velasco Erick Iram',
    'Gónzalez Castro Diego Daniel',
    'Hernández Vela Daniel',
    'Isunza Álvarez Marcos Guillermo',
    'López Miranda Angel Mauricio',
    'López Prado Emiliano',
    'Monterrubio Acosta Demian Alejandro',
    'Navarro Santana Pablo César',
    'Ortíz Amaya Bruno Fernando',
    'Reyes López Eduardo Alfonso',
    'Reyes Trujillo Guadalupe',
    'Ríos Raúl', 
    'Trujillo Beltrán Zianya Nenetzi', 
    'Verano Peralta María Fernanda',
    'Vázquez Kuri Eduardo', 
    'Zurita León Dana Cecilia']

for a in alumnos:
    if aprueba_alumno(a):
        print('APROBADOO: ' + a)
    else:
        print('REPROBADO: ' + a)

print(aprobados)
print(borra_alumno('Abaustista Erick'))
print(aprobados)
