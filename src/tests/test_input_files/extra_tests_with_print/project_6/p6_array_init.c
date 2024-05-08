#include <stdio.h>

int main(){
    int values[3] = {3, 45, -9};
    printf("values[0] = %d\n", values[0]);
    values = {-22, 7896, 1};
    printf("values[0] = %d\n", values[0]);
    int other[3][4];
    other[2] = {1,2,6,93};
    printf("other[2][0] = %d\n", other[2][0]);

    return 0;
}