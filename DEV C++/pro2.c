#include<stdio.h>
#include<conio.h>
int main()
{
	int a[20],n,i,j,swap;
	printf("Enter the size of array:");
	scanf("%d",&n);
	printf("\n Eneter %d elements to be stored in the array:\n",n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
		for(i=0;i<n-1;i++)
		{
			for(j=0;j<n-i-1;j++)
			{
				if(a[j]>a[j+1])
				
				{
					swap=a[j];
					a[j]=a[j+1];
					a[j+1]=swap;
				}
				
			}
		}
	printf("\n sorted Array:");
	for(i=0;i<n;i++)
	printf("%d",a[i]);
	printf("\n");
	
}
