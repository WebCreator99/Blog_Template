
# include<stdio.h> 
void heapify(int a[], int n, int i) 
{ 
    int largest = i; 
    int left = 2 * i + 1; 
    int right = 2 * i + 2; 
 
    if(left < n && a[left] > a[largest]) 
    { 
 largest = left; 
    } 
 
    if(right < n && a[right] > a[largest]) 
    { 
   largest = right; 
    } 
    if(largest !=i) 
    { 
    int temp; 
    temp = a[i]; 
    a[i] = a[largest]; 
    a[largest] = temp; 
    heapify(a,n,largest); 
    } 
} 
 
void HEAPSORT(int a[], int n) 
{ 
   int i;  
   for(i=n/2-1;i>=0;i--) 
   heapify(a,n,i); 
   for( i=n-1; i>=0; i--) 
   { 
   int temp; 
   temp = a[0]; 
   a[0] = a[i]; 
   a[i] = temp; 
   heapify(a,i,0); 
    } 
} 
void printArr(int arr[], int n) 
{ 
  int i; 
  for( i=0; i<n; ++i) 
  { 
     printf("%4d",arr[i]); 
  } 
} 
void main() 
{ 
int a[] = { 9,16,32,8,4,1,5,8,0 }; 
int n = sizeof(a) / sizeof(a[0]);  
printf("\n Before sorting : "); 
printArr(a,n); 
HEAPSORT(a,n); 
printf("\n After sorting : "); 
printArr(a,n); 

}
