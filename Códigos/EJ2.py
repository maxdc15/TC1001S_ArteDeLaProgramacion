# Para correr el programa: python EJ2.py

# Este progrma simula el lanzmiento de un dado
import random

# constantes para el valor mínimo y máximo del dado
MIN = 1
MAX = 6

def main():
    # crear una variable para el control de un loop
    again = 'y'
    
    # Simular en lanzamiento de un dado
    while again == 'y' or again == 'Y':
        print('Rolling the dice...')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        
        # Hacer otro lanzamiento de dados?
        again = input('Roll them again? (y = yes): ')
        
# Llamar a la función main
main()