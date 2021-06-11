#include<stdio.h>
#include<string.h>
int main()
{
	char st[100];
	int arr[10],i,j,l;
	gets(st);
	
	for(l=0;l<10;l++)
	{
		arr[l]=0;
	}
	
	for(i=0;st[i]!=NULL;i++)
	{
		
		if(st[i]=='0')
			arr[0]+=1;
			
		if(st[i]=='1')
			arr[1]+=1;
			
		if(st[i]=='2')
			arr[2]+=1;
			
		if(st[i]=='3')
			arr[3]+=1;
			
		if(st[i]=='4')
			arr[4]+=1;
			
		if(st[i]=='5')
			arr[5]+=1;
			
		if(st[i]=='6')
			arr[6]+=1;
			
		if(st[i]=='7')
			arr[7]+=1;
			
		if(st[i]=='8')
			arr[8]+=1;
			
		if(st[i]=='9')
			arr[9]+=1;
	}
	
	for(j=0;j<10;j++)
	{
		printf("%d ",arr[j]);
	}
	
	return 0;
}
