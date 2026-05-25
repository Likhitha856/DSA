# import array as a
# import array as a
import numpy as np
nums=np.array([[1,2,3],[4,5,6]])

def sum(arr):
    sum=0
    for i in range(len(arr)):
        for j in range (len(arr[i])):
            sum+=arr[i][j]
    return sum

print(sum(nums))

def transpose(nums):
    rows=len(nums)
    cols=len(nums[0])
    transp=np.empty((cols,rows))
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            transp[j][i]=nums[i][j]
    return transp
print(transpose(nums))