#include <stdio.h>

void function1() {
    int a = 5;
    printf("a: %d\n", a);
    return;
}

void function2() {
    int a = 10;
    printf("a: %d\n", a);
    return;
}

int main() {
    function1();
    function2();
    return 0;
}