#include <stdio.h>

int main() {
    int a = 5;
    if (a > 10) {
        printf("a is greater than 10\n");
    } else if (a > 3) {
        printf("a is greater than 3\n");
    } else {
        printf("a is not greater than 3\n");
    }
    return 0;
}