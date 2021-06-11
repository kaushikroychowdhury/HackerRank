#include<stdio.h>
int main()
{
	char ch,s[50],st[50];
	
	scanf("%c",&ch);
	scanf("%s",s);
	scanf(" %[^\n]%*c",st);
	
	
	printf("%c\n",ch);
	printf("%s\n",s);
	printf("%s",st);
	
	return 0;
}
