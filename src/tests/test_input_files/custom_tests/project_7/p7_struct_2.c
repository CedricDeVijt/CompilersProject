#include <stdio.h>

struct test{
    int a;
    float b;
    char c;
};

int main(){
    struct test t = {10, 3.14, 'A'}; // definition
    int a = t.a;
    return 0;
}