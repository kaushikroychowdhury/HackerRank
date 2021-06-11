#include<stdio.h>
int main()
{
	int n,m;
	float f,q;
	
	scanf("%d %d", &n, &m);
	scanf("%f %f", &f, &q);
	
	printf("%d %d\n", n+m, n-m);
	printf("%0.1f %0.1f", f+q, f-q);
	
	return 0;
}
