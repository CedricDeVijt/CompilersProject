#include <stdio.h>

enum week {Mon, Tue, Wed, Thu, Fri, Sat, Sun};

int main() {
    int a = (Wed + Thu) * Sun;
    printf("%d", a);
}