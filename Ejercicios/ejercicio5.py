#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice
import csv 
import os 

archivo = open('lista_completa.txt', "r", encoding = "utf-8")
lineas = archivo.readlines()
contenido = archivo.read()
archivo.close()


becarios1 = []
for linea in lineas:
    becarios1.append(linea.strip())


calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios2 = [
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
    for b in becarios1:
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

def escribir_csv(diccionario, calificaciones_csv):
    #Comprobamos que el diccionario no se encuentre vacío
    if not diccionario:
        print("El diccionario se encuentra vacío. No se puede crear un archivo csv")
        return 
    
    #Abrimos/creamos el archivo CSV en modo escritura
    with open(calificaciones_csv, mode = 'w', newline = '' ) as archivo:
        #Creamos un objeto escritor de CSV
        writer = csv.writer(archivo)
        
        #Escribimos las cabeceras usando las claves del diccionario
        writer.writerow(diccionario.keys())
        
        #Escribimos las filas del CSV
        #Usamos zip para agrupar los valores de todas las listas dentro del diccionario 
        #para escribirlos como filas del CSV
        writer.writerow(diccionario.values())
        
        

asigna_calificaciones()
imprime_calificaciones()
aprobados, reprobados = alumnos_aprobados_reprobados()
print("Aprobados: ", aprobados)
print("Reprobados: ", reprobados)
print(promedio())
print(calificaciones_obtenidas())
print(type(contenido))
#escribir_csv(becarios1)
print(becarios1)
escribir_csv(calificacion_alumno, 'calificaciones.csv')

