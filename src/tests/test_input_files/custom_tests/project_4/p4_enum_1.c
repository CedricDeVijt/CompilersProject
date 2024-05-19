#include <stdio.h>

enum Numbers {
    ZERO,
    ONE,
    TWO
};

int main() {
    enum Numbers a = ONE;
    if (a == ONE) {
        printf("a is ONE\n");
    }
    return 0;
}