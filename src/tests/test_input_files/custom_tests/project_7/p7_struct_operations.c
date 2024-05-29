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
    t.a++;
    ++t.a;
    t.b = 20 + 5;
    t.c = 23.6;
    t.b--;
    t.d = 'h';
    t.d = 'i';
    printf("%d, ,%d, %f, %c\n", t.a, t.b, t.c, t.d);
    return 0;
}