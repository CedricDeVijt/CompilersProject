#include <stdio.h>

int main() {
    int a = 5;
    printf("%d\n", a);
    int b = 10;
    printf("%d\n", b);
    int* p = &a;
    printf("%d\n", *p);
    p++;
    printf("%d\n", *p);
}