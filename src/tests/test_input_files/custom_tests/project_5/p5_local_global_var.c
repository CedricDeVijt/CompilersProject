#include <stdio.h>

int a = 5;

void function1() {
    int b = 10;
    printf("a: %d, b: %d\n", a, b);
    return;
}

int main() {
    function1();
    return 0;
}