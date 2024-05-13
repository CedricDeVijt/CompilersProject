#include <stdio.h>

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int *b = &a[0];
    printf("%d\n", *b);
    b++;
    printf("%d\n", *b);
    return 0;
}