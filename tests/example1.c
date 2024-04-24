#include <stdio.h>

int test(int a) {
    return a+a;
}

int main()
{
    float a = 1+test(5);
    printf("string: %s, float: %f", "test", a);
    return 0;
}