typedef int testType;

int main() {
    int a = 5;
    switch (a) {
        case 4:
            a = 5;
        case 69:
            a = 6;
            break;
        case 5:
            a = 10;
        default:
            a = 20;
            break;
    }
    printf("%d", a);
}