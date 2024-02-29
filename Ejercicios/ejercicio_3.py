#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = [
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

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('%s tiene %s\n' % (alumno,calificacion_alumno[alumno]))

def alumnos_aprobados_reprobados():
    alumnos_aprobados = []
    alumnos_reprobados = []
    for alumno in calificacion_alumno:
        if(calificacion_alumno[alumno] >= 8):
            alumnos_aprobados.append(alumno)
        else:
            alumnos_reprobados.append(alumno)
    aprobados = tuple(alumnos_aprobados)
    reprobados = tuple(alumnos_reprobados)
    return  aprobados, reprobados
  
def promedio():
    return sum(calificacion_alumno.values()) / len(calificacion_alumno)

def calificaciones_obtenidas():
    calificaciones_obtenidas = set(calificacion_alumno.values())
    return calificaciones_obtenidas

asigna_calificaciones()
imprime_calificaciones()
aprobados, reprobados = alumnos_aprobados_reprobados()
print("Aprobados: ", aprobados)
print("Reprobados: ", reprobados)
print(promedio())
print(calificaciones_obtenidas())