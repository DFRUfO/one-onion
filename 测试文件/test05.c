#include<stdio.h>
int main()
{   
	int max(int *a,int n);
	int i,n,a[20],d;
	printf("please enter the numbers length:");
	scanf("%d",&n);
	printf("please enter %d numbers:",n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	d=max(a,n);
	printf("max is %d",d);
	return 0;
}//这是注释行1

//这是注释行2
int max(int *a,int n)
{
	int i,j,c,b,z,m;
    for(i=0,j=1;j<n;i++,j++)
	{   
		c=*(a+i);
	    b=*(a+j);
		if(c>b)
		{   
			z=c;
			c=b;
			b=z;
		}
		else
			z=b;
	}
	m=z;
	return m;
}
