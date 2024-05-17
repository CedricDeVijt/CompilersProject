#include <stdio.h>

int main() {
    printf("%d\n", (5 & 3) | 2);
    printf("%d\n", ~(5 | 3));
    printf("%d\n", (5 ^ 3) & 4);
    return 0;
}