#include <stdio.h>

int main(){
    int values1[5][3][4];
    values1[0][0][0] = 1;

    printf("%d\n", values1[0][0][0]);

    values1[1][0] = {1,2,3,4};


    return 0;
}