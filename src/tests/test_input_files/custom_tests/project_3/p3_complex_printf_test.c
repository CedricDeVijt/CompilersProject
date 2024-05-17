#include <stdio.h>

int main() {
    int a = 5;
    float b = 3.14;
    printf("%d\n", a + (int)b);
    printf("%f\n", b + (float)a);
    return 0;
}