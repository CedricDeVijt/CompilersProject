#include <stdio.h>

struct test{
    int a;
    int b;
    float c;
    char d;
};

struct test2{
    int a;
    int b;
    float c;
    char d;
};

int main(){
    struct test t = {10, 20, 23.6, 'h'};
    struct test2 t2 = {15, 36, 18.98, '4'};
    printf("%d, ,%d, %f, %c\n", t.a, t.b, t.c, t.d);
    printf("%d, ,%d, %f, %c\n", t2.a, t2.b, t2.c, t2.d);
    return 0;
}