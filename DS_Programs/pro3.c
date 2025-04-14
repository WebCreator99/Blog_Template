#include<stdio.h>
#include<conio.h>
int gcd(int m, int n)
{
	if(n==0)
	{
		return(m);
	}
	else if(n>m)
	{
		return(gcd(n,m));
	}
	else
	{
		return(gcd(n,m%n));
	}
}
void main()
{
	int k,m,n;
	printf("Enter th numbers:\n");
	scanf("%d%d%d",&k,&m,&n);
	printf("\nGCD of(%d%d%d)=%d\n",m,n,gcd(k,gcd(m,n)));
	getch();
	
}
