nums=[1,2,3,4]
def concat(nums):
    ans=[]
    n=len(nums)*2
    for i in range(n):
        if i<=len(nums)-1:
            ans.append(nums[i])
        else:
            x=i%len(nums)
            ans.append(nums[x])
    return ans
print(concat(nums))