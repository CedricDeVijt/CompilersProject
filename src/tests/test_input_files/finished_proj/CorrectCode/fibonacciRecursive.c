
#include <stdio.h>

int f(int a) {
	if (a<2) {
		return a;
	}
	else {
		return f(a-1) + f(a-2);
	}
}

// Recursive Fibonacci
int main(){
	int n = 10;
	int i = 1;
	while(i++ <= n){
	    number = f(i);

		printf("fib(%d)\t= %d;\n", i, number);
	}
	return 0;
}
