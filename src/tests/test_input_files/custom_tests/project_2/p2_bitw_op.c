#include <stdio.h>

int main() {
    int a = 15;
    int b = 3;
    printf("%d\n", a&b);
    printf("%d\n", a|b);
    printf("%d\n", ~a);
    printf("%d\n", a^b);

    return 0;
}