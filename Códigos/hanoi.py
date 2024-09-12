# Recursive implementation to solve the Towers of Hanoi problem

steps = 1
# Complexity O(2^N)
def hanoi(n: int, orig, aux, dest):
    global steps
    if n == 1:
        print(f'{steps}. Move disk 1 from {orig} to {dest}')
        steps += 1
    else:
        hanoi(n-1, orig, dest, aux)
        print(f'{steps}. Move disk {n} from {orig} to {dest}')
        steps += 1
        hanoi(n-1, aux, orig, dest)

def main():
    n = int(64)
    hanoi(n, 'A', 'B', 'C')

main()