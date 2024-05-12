#include <stdio.h>

typedef int MyType;

int main() {
    typedef float MyType;
    MyType a = 5.5;
    printf("%f\n", a);
    return 0;
}