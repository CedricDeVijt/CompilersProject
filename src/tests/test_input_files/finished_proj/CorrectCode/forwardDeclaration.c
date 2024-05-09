#include <stdio.h>

void f();

void g();

void f(){
	printf("Hello ");
	return;
}

void g(){
	printf("World\n");
	f();
	printf("World\n");
	return;
}

int main(){
	f();
	g();
	return 0;
}
