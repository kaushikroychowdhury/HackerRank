#include<stdio.h>
#include<string.h>
#include<string.h>

int main()
{
	char s[1024];
	int i=0;
	
	gets(s);
	
	for(i=0;s[i]!=NULL;i++)
	{
		if(s[i]==' ')
			printf("\n");
			
		else
			printf("%c",s[i]);

	}
	
	return 0;
}
