#include <stdio.h>

int main(){
    int values1[5][3][4]= {
        { {1,2,3,4}, {5,6,7,8}, {9,10,11,12} },
        { {13,14,15,16}, {17,18,19,20}, {21,22,23,24} },
        { {25,26,27,28}, {29,30,31,32}, {33,34,35,36} },
        { {37,38,39,40}, {41,42,43,44}, {45,46,47,48} },
        { {49,50,51,52}, {53,54,55,56}, {57,58,59,60} }
    };

    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 3; j++){
            for (int k = 0; k < 4; k++){
                values1[i][j][k] = 5;
                printf("values1[%d][%d][%d] = %d\n", i, j, k, values1[i][j][k]);
                printf("values1[%d][%d][%d] = %d\n", i, j, k, values1[i][j][k]);
                printf("values1[%d][%d][%d] = %d\n", i, j, k, values1[i][j][k]);
                printf("values1[%d][%d][%d] = %d\n", i, j, k, values1[i][j][k]);
                printf("values1[%d][%d][%d] = %d\n", i, j, k, values1[i][j][k]);
                printf("values1[%d][%d][%d] = %d\n", i, j, k, values1[i][j][k]);
                printf("values1[%d][%d][%d] = %d\n", i, j, k, values1[i][j][k]);
                printf("values1[%d][%d][%d] = %d\n\n", i, j, k, values1[i][j][k]);
            }
        }
    }

    return 0;
}