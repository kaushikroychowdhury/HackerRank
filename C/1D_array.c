#include<stdio.h>

int main()
{
	int i,n,sum=0;
	scanf("%d",&n);
	int *arr = malloc(n*sizeof(int));
	
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
		sum+=arr[i];
	}
	
	printf("%d",sum);
	free(arr);
	
	return 0;
}