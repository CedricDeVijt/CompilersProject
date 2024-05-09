#include <stdio.h>

int main() {
    int x = 2;
    switch (x) {
        case 1:
            printf("%d", 1);
            break;
        case 2:
            printf("%d", 2);
        default:
            printf("%d", 999);
            break;
    }
    return 0;
}