#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
	int area;
};

typedef struct triangle triangle;
void sort_by_area(triangle tr[], int n) {
	/*
	* Sort an array a of the length n
	*/
	
	triangle temp;
	int i,j,p;
	
	for(i=0;i<n;i++)
	{
		p = (tr[i].a + tr[i].b + tr[i].c)/2;
		
		tr[i].area = sqrt(p*(p-tr[i].a)*(p-tr[i].b)*(p-tr[i].c));
	}
	
	i=0;
	
	while(i<n)
	{
		for(j=i+1;j<n;j++)
		{
			if(tr[i].area > tr[j].area)
			{
				temp=tr[i];
				tr[i]=tr[j];
				tr[j]=temp;
			}
		}
		i++;
	}
}

int main()
{
	int n,i;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for(i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for(i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}

