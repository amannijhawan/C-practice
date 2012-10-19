#include <stdio.h>

int iterative_gcd(int u, int v) {
	int t;
	int i;
	i=0;
	while(u>0) {
		i++;
		printf("%d %d\n", u, v);
		if (u < v) {
			t = u;
			u = v;
			v = t ; 
		}
		u = u-v;
	}
	printf("%d %d\n", u, v);
	printf("Statements Executed: %d\n",i+6);	
	return v;
}

int recursive_gcd_1(int u, int v){
	if ((u % v) == 0)
		return v;
	else
		return recursive_gcd_1(v,u%v);
}

int recursive_gcd_2(int u, int v) {
	if (u > v)
		return recursive_gcd_2(u-v,v);
	else if (v>u)
		return recursive_gcd_2(v-u,u);
	else if (u==v)
		return u;
}
			

