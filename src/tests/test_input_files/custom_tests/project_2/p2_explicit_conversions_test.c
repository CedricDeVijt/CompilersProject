#include <stdio.h>

typedef int myInt;
typedef float myFloat;

int main() {
    myInt a = 5;
    myFloat b = 3.14;
    printf("%d\n", a + (myInt)b);
    printf("%f\n", b + (myFloat)a);
    return 0;
}