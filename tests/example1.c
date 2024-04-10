typedef int testType;

int main() {
    int a = 5;
    switch (a) {
        case 5:
            testType b = 5;
            break;
        default:
            int b = 6;
            break;
    }
    printf("%d", a);
}