#include <stdio.h>

int main() {
    int x = 10;
    {
        int x = 20;
        printf("%d", x);
    }
    printf("%d", x);
    return 0;
}