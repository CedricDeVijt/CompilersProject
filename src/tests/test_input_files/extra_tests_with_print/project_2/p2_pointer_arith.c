#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int* p = &a;
    printf("%d\n", a);
    printf("%d\n", b);
    printf("%d\n", *p);
    p++;
    printf("%d\n", *p);
}