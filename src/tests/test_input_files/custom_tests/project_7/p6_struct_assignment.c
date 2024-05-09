#include <stdio.h>

struct test{
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
    t.a = 10+10;
    t.b = 20*5;
    t.c = 23.6-3.7;
    t.d = 'k';
    printf("%d, ,%d, %f, %c\n", t.a, t.b, t.c, t.d);
    return 0;
}
