#include<stdio.h>


int binary(int x) {
		if (x == 0 ||  x == 1){
			printf("%d", x);
			return;}
		
	 	binary(x/2);
		printf("%d",x%2);
		}
main() {
	int i ;
	for(i=0; i < 128; i++){
		printf("%d\t", i);
		binary(i);
		printf("\n");
}
}

