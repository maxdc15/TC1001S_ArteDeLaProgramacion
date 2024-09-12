#include <iostream>
// 1. Move n - 1 discs from orig to aux (using dist as auxiliary)
// 2. Move disc n from orig to dest

// Complexity O(2^N)
void hanoi(int n, char orig, char aux, char dest)
{
    static int step = 1;

    if (n == 1) {
        std::cout << step <<  ". Move disc 1 from " << orig << " to " << dest << '\n';
        step++;
    } else {
        hanoi(n - 1, orig, dest, aux);
        std::cout << step << ". Move disc " << n << " from " << orig << " to " << dest << '\n';
        step++;
        hanoi(n - 1, aux, orig, dest);
    }
}

int main()
{
    hanoi(6, 'A', 'B', 'C');
    return 0;
}