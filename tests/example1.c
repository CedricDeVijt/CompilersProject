typedef float testType;

int main() {
    int a = 5;
    a = !a;
    a = a+a/a+a;
    float b = (int) 5.0;
    // Test
    if (a==a) {
        testType a = 5.0;
        printf("%f", a);
    }
    int c = 0;
    int* d = &c;
    int** e = &d;
    a = **e;
    while(a<500) {
        a++;
        printf("%d", a);
    }
}