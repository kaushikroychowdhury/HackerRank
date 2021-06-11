#include<stdio.h>

int max_of_four(int a, int b, int c, int d)
{
	if(a>b && a>c && a>d)
		return a;
		
	if(b>a && b>c && b>d)
		return b;
		
	if(c>a && c>b && c>d)
		return c;
		
	else
		return d;
}

int main()
{
	int max=0,h,g,f,e;
	scanf("%d",&e);
	scanf("%d",&f);
	scanf("%d",&g);
	scanf("%d",&h);
	
	
	max=max_of_four(e,f,g,h);
	printf("%d", max);
	
	return 0;
}
