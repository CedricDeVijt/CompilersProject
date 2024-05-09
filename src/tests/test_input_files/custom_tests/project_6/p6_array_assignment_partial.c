#include <stdio.h>

int main(){
    int values1[5][3][4];
    values1[0][0][0] = 1;
    printf("%d\n", values1[0][0][0]);

    values1[1][0] = {8,8,8,8};
    printf("%d\n", values1[1][0][0]);

    return 0;
}