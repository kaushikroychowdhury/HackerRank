#include<stdio.h>
#include<stdlib.h>

int marks_summation(int* marks, int n, char gender)
{
	int sum=0, i;
	if(gender=='b')
	{
		for(i=0;i<n;i++)
		{
			if(i%2==0)
			{
				sum+=marks[i];
			}
		}
		return sum;
	}
	
	if(gender=='g')
	{
		for(i=0;i<n;i++)
		{
			if(i%2!=0)
			{
				sum+=marks[i];
			}
		}
		return sum;
	}
}

int main()
{
	int n,i,sum;
	char gender;
	scanf("%d",&n);
	
	int *marks = (int *) malloc(n*sizeof(int));
	
	for(i=0;i<n;i++)
	{
		scanf("%d",&marks[i]);
	}
	
	scanf(" %c",&gender);
	sum=marks_summation(marks,n,gender);
	printf("%d",sum);
	
	return 0;
}
