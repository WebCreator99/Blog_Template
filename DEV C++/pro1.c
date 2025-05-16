#include<stdio.h>
#include<conio.h>
void main()
{
	int a[20],n,i,x;
	printf("Enter the size of the array:");
	scanf("%d",&n);
	printf("\n Enter %d elements to be stored in the array:\n",n);
	for(i=0;i<n;++i)
	scanf("%d",&a[i]);
	printf("\n Enter the element to be  searched:");
	scanf("%d",&x);
	for(i=0;i<n;++i)
	{
		if(a[i]==x)
		break;
	}
	if(i<n)
	printf("\n Element is found at position:%d",i+1);
	else
	printf("\n Enetered element is not found\n");
}


