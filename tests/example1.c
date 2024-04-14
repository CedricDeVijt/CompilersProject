void test() {
    printf("%d", 5);
    return;
}

int test(int &a) {
    a = 20;
    return 0;
}

int mul(int a, int b) {
    return a*b;
}

int main() {
    int a = 5;
    char endline = 'a';
    printf("%d", a);
    printf("%c", endline);
    test(a);
    printf("%d", a);
    printf("%c", endline);
    int b;
    a = mul(a, b);
    printf("%d", a);
    printf("%c", endline);
    return 0;
}