def build_arr(nums):
    length=len(nums)
    new=[]
    for i in range(len(nums)):
        x=nums[i]
        new.append(nums[x])
    return new
nums=[0,2,1,5,3,4]
print(build_arr(nums))