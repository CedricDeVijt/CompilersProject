#include <stdio.h>

struct test{
    int a;
    float b;
    char c;
};

int main(){
    struct test t;
    t.a = 10;
    t.b = 20.5;
    t.c = 'A';
    printf("%d, %f, %c\n", t.a, t.b, t.c);
    return 0;
}
