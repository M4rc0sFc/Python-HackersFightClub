#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice
from poo1 import Alumno 


calificacion_alumno = []
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
        calificacion_alumno.append(Alumno(b,choice(calificaciones)))

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('El alumno %s tiene calificacion %d' %(alumno.get_nombre(), alumno.get_calificacion()))
  
def calificaciones_obtenidas():
    calificaciones_obtenidas = []
    for alumno in calificacion_alumno:
        calificaciones_obtenidas.append(alumno.get_calificacion())
    return calificaciones_obtenidas

def ImprimeCalificacion():
    for alumno in calificacion_alumno:
        print('El alumno %s tiene calificacion %d', alumno.get)

asigna_calificaciones()
imprime_calificaciones()
print(calificaciones_obtenidas())
