#include <stdio.h>

enum week{Mon, Tue, Wed};

int main () {
    int a = Wed + Wed;
    int b = a;
    printf("%d\n", b);
    return 0;
}