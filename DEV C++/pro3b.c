#include<stdio.h>
#include<conio.h>
int main()
{
	int a[20],n,i,j,position,swap;
	printf("Enter the size of the array:");
	scanf("%d",&n);
	printf("\n Enter %d element to be stored in the array:\n",n);
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=0;i<n-1;i++)
	{
		position=i;
		for(j=i+1;j<n;j++)
		{
			if(a[position]<a[j])
			position=j;
		}
	
	if(position!=i)
	{
		swap=a[i];
		a[i]=a[position];
		a[position]=swap;
	}
}
	printf("\n Sorted Array:");
	for(i=0;i<n;i++)
	printf("%d",a[i]);
	printf("\n");
	
}
