#include <stdio.h>

int main() {
    int a = 5;
    printf("%d\n", a);
    int* p = &a;
    printf("%d\n", *p);
    *p = 10;
    printf("%d\n", a);

    return 0;
}