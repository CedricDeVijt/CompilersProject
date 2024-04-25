#include <stdio.h>

#ifndef test
#define test
int a = 10;
#endif

#ifndef test
#define test
int a = 5;
#endif


int main()
{
    printf("%d", a);
    return 0;
}