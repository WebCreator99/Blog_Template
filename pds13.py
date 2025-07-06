arr=[10,20,30,40,50]
ele=50
pos=-1
low=0
high=len(arr)-1

while(low<=high):
    mid=(low+high)//2;
    if(arr[mid]==ele):
        pos=mid
        break
    elif(arr[mid]>ele):
        high=mid-1
    else:
        low=mid+1
print(pos)