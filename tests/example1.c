int a = 1+1;

int main() {
    int a = 5;
    int* p = &a;
    int** p1 = &p;
    **p1 = 10;
}
