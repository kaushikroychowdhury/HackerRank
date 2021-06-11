#include<stdio.h>

int main()
{
	int n,k,max=0,a,max2=0,max3=0;
	
	scanf("%d %d",&n,&k);
	
	int t=n-1,i,j;
	
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=t;j++)
		{
			a=i&(i+j);
			if(a>max && a<k)
			{
				max=a;
			}
		}
		t--;
	}
	
	t=n-1;
	
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=t;j++)
		{
			a=i|(i+j);
			if(a>max2 && a<k)
			{
				max2=a;
			}
		}
		t--;
	}
	
	t=n-1;
	
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=t;j++)
		{
			a=i^(i+j);
			if(a>max3 && a<k)
			{
				max3=a;
			}
		}
		t--;
	}
	
	printf("%d\n",max);
	printf("%d\n",max2);	
	printf("%d",max3);
	return 0;
}
