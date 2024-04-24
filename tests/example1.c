#include <stdio.h>

int main() {
    int a = 10;
    int b = 0;
    switch (a)
    {
    case 1:
        b = 1;
        break;
    case 3:
        b = 3;
    case 10:
        b = 10;
    }
    return 0;
}