#include<stdio.h>

int main()
{
	int b,i,j,k,l,m,n;
	scanf("%d",&b);
	
	for(i=b;i>=1;i--)
	{
		for(j=b;j>=1;j--)
		{
			if(j<=i)
				printf("%d ",i);
				
			else
				printf("%d ",j);
		}
		
		for(k=2;k<=b;k++)
		{
			if(k<=i)
				printf("%d ",i);
				
			else
				printf("%d ",k);
		}
		
		printf("\n");
	}
	
		for(l=2;l<=b;l++)
	{
		for(m=b;m>=1;m--)
		{
			if(m<=l)
				printf("%d ",l);
				
			else
				printf("%d ",m);
		}
		
		for(n=2;n<=b;n++)
		{
			if(n<=l)
				printf("%d ",l);
				
			else
				printf("%d ",n);
		}
		
		printf("\n");
	}
}
