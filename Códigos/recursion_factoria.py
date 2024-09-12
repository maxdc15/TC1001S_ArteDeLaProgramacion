# código para obtener el factoria de un número de forma recursiva

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def main():
    # Número limite: n = 996
    print(factorial(996))
    
main()
