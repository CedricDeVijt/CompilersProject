
int main() {
    int a = 5;
    for(int i=0; i<50; i++) {
        printf("%d", i);
    }
    for(;;) {
        break;
    }
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