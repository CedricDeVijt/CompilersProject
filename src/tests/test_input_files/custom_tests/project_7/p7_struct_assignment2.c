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
    t.b = 20;
    t.c = 23.6;
    t.d = 'h';
    printf("%d, ,%d, %f, %c\n", t.a, t.b, t.c, t.d);
    struct test2 t2;
    t2.a = 10+10;
    t2.b = 20*5;
    t2.c = 23.6-3.7;
    t2.d = 'k';
    printf("%d, ,%d, %f, %c\n", t.a, t.b, t.c, t.d);
    return 0;
}