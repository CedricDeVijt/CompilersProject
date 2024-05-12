#include <stdio.h>

typedef int myInt;
typedef float myFloat;
typedef char myChar;

int main() {
    myInt a = 5;
    printf("%d", a);
    myFloat b = 5.5;
    printf("%f", b);
    myChar c = 'c';
    printf("%c", c);
    return 0;
}