#include <stdio.h>

int main() {
    int a = 15;
    int b = 3;
    printf("%d\n", !(a < b) && (a > b));
    printf("%d\n", (a == b) || !(a != b));

    return 0;
}
