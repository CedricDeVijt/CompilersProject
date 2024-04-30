int add(int x, int y) { return x + y;}
int add(int x, int y, int z) { return x + y + z;}
float add(float a, float y) { return a + y;}

int main() {
    int a = add(1, 2);
    int b = add(1, 2, 3);
    float c = add(1.1, 2.2);
    return 0;
}