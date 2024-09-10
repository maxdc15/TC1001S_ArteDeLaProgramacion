# Hacer la secuencia de Fibonnaci mediante el uso de la recursión
# Fn = (Fn - 1) + (Fn - 2) 

def fibonacci(n):
    a = int(0)
    b = int(1)
    print(a, b, end=' ')
    for i in range(2, n+1):
        c = int(a+b)
        print(c, end=' ')
        a = b
        b = c
        
def fibo_list(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[i-1]+F[i-2])
    return F

def recursive_fibonacci(n):
     return n if n < 2 else recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
 
def recursive_fibo(n, fib_sequence=None):
    # Lista para acumular los resultados
    if fib_sequence is None:
        fib_sequence = []

    # Caso base
    if n == 0:
        fib_sequence.append(0)
        return fib_sequence
    elif n == 1:
        fib_sequence.extend([0, 1])
        return fib_sequence
    
    # Si aún no se ha calculado, llamar recursivamente
    fib_sequence = recursive_fibo(n-1, fib_sequence)
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

def main():
    print(fibonacci(10))
    print(fibo_list(10))
    print(recursive_fibonacci(10))
    print(recursive_fibo(10))

main()