def linear_Serach(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
           return i
    return -1       


arr=[2,4,6,8,10]
target=96
result=linear_Serach(arr,target)

if(result!=-1):
    print("Element found")
else:
    print("Element is not found")    