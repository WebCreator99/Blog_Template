#include<stdio.h>
#include<conio.h>
void main()
{
	int a[20],n,low,high,mid,i,key;
	printf("Enter the size of the array:");
	scanf("%d",&n);
	printf("\n Enter %d elements to be stored in the array:\n",n);
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	printf("\n Enter the element to be  searched:");
	scanf("%d",&key);
	low=0;
	high=n-1;
	mid=(low+high)/2;
	while(low<=high)
	{
		if(a[mid]<key)
		low=mid+1;
		else if(a[mid]==key)
		{
			printf("\n element found at position %d:",mid+1);
			break;
			
		}
		else
		high = mid-1;
		mid =(low+high)/2;
	}
	if(low>high)
	printf("\n Entered element not found\n");
}
	

