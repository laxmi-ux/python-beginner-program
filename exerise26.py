def binary_search(arr,target):
    low=0
    high=len(arr)

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1        
    return -1        


arr=[2,4,6,8,10,12,24]
target=12
result=binary_search(arr,target)

if result!=-1:
    print("Element is found")

else:
    print("Element is not found")    
