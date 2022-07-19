# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:24:14 2022

@author: uli_r
"""

'''
Genere un programa que tenga un menú 
en el cual el usuario pueda seleccionar
entre las siguientes opciones:

(1) Saludar: esta opción debe pedir el nombre al usuario y saludarlo.
(2) Tirar un dado: esta debe generar aleatoriamente un número y mostrarlo.
(3) Salir: esta opción debe terminar el programa.

En caso de elegir entre las opciones (1) y (2), el programa deberá realizar la acción correspondiente y volver a mostrar el menú.

Si no se elige ninguna de las opciones, el programa deberá mandar un mensaje de que la opción no es válida y volver a mostrar el menú.
'''

######## Librerías ########
from random import randint
from os import system

######## Funciones ########
def saludar():
    nombre = input("\n¿Cuál es tu nombre? ")
    print(f"\nHola estimade {nombre}")
    
def tirar_dado():
    dado = randint(1,6)
    print(f"\nEl dado salió: {dado}")
    
    
    
######## Programa principal ########
def main():
    while True:
        opcion = input("""Introduce el número de una opción del menú:
              
              (1) Saludar
              (2) Tirar un dado
              (3) Salir
              
              Opción: """)
        
        if opcion == '1':
            saludar()
        elif opcion == '2':
            tirar_dado()
        elif opcion == '3':
            break
        else:
            print('Tu opción es inválida.')
        
        print("\n-----------------------------\n")
        input("Presiona Enter para continuar...\n\n")
        
        system('cls')
    
if __name__ == '__main__':
    main()


