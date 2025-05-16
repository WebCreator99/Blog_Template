#include<stdio.h>
#include<conio.h>
int main()
{
	int a[20],i,j,size,swap;
	printf("Enter the size of the array:");
	scanf("%d",&size);
	printf("\n Eneter %d element stored in the array:\n",size);
	for(i=0;i<size;i++)
	scanf("%d",&a[i]);
	for(i=1;i<(size);i++)
	{
		j=i;
		while(j>0&&a[j]>a[j-1])
		{
			swap=a[j];
			a[j]=a[j-1];
			a[j-1]=swap;
			j--;
		}
	}

printf("\n Soted array:");
for(i=0;i<size;i++)
printf("%d",a[i]);
printf("\n");
}

