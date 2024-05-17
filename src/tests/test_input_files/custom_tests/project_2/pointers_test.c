#include <stdio.h>

int main() {
    int a = 5;
    int* p = &a;
    *p = 10;
    printf("a: %d\n", a);
    return 0;
}