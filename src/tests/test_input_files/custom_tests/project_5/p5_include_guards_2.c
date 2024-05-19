#ifndef MY_HEADER_H
#define MY_HEADER_H

#include <stdio.h>

#endif

#ifndef ANOTHER_HEADER_H
#define ANOTHER_HEADER_H

#include "/src/tests/test_input_files/custom_tests/project_5/p5_include_header.h"

#endif

int main() {
    printf("The value of a is: %d", a);
    return 0;
}