#include<stdio.h>

int main()
{
	int n=0,m=0,l=0,temp=0;
	scanf("%d",&n);
	int arr[n];
	int i=0,j=n-1;
	
	for(m=0;m<n;m++)
	{
		scanf("%d",&arr[m]);
	}
	
	while(i<j)
	{
		
		temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
		
		i++;
		j--;
	}
	
	for(l=0;l<n;l++)
	{
		printf("%d ",arr[l]);
	}
	
	return 0;
}
