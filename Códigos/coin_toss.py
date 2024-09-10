# Este programa simula lanzamientos de una moneda
import random

def main():
    
    heads = 0
    tails = 0
    rango = 100000
    for i in range(rango):        
        # si el número es 0, es águila
        if random.randint(0, 1):
            heads += 1
        # si el número es 1, es sol
        else:
            tails += 1
     
    # porcentaje de águilas y de sol
    porcenajes_aguila = (heads / rango)
    porcetajes_sol = (tails / rango)
    print(f'Porcentaje de águilas: {porcenajes_aguila:.2%}')
    print(f'Porcentaje de sol: {porcetajes_sol:.2%}')
 
main()