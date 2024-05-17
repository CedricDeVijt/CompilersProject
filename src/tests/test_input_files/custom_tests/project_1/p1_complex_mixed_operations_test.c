#include <stdio.h>

int main() {
    printf("%d\n", ((5 + 3) * 2) >> 1);
    printf("%d\n", ~((10 - 2) / 2));
    printf("%d\n", (5 * 3) % 7 && 1);
    printf("%d\n", 6 / 3 * 2 > 3);
    return 0;
}