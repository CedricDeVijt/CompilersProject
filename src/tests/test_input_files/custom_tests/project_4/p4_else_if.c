#include <stdio.h>

int main() {
    int x = 10;
    if (x > 10) {
        printf("%d>10", x);
    } else if (x == 10) {
        printf("%d==10", x);
    } else {
        printf("%d<10", x);
    }
    return 0;
}