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
    struct test t;
    t.a = 10;
    int a = t.a;
    t.b = 20;
    t.c = 23.6;
    t.c = 47.79;
    float c = t.c;
    t.d = 'h';
    char d = t.d;
    t.d = 'g';
    printf("%d, ,%d, %f, %c\n", t.a, t.b, t.c, t.d);
    printf("%d, %f, %c\n", a, c, d);
    t.a = t.b;
    t.b = a;
    t.c = c;
    t.d = d;
    printf("%d, ,%d, %f, %c\n", t.a, t.b, t.c, t.d);
    return 0;
}