# Manejo de la librería random de Python
# Por: Maximiliano De La Cruz Lima
# Creado: 9/Septiembre/2024
import random as rand

def numeros_aleatorios():
    num = rand.randint(1, 10);
    print(num, end=" ");
    
def main():
    for i in range(10):
        numeros_aleatorios();
        
main()
    