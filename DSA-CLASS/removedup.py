nums=[1,2,2,2,3,3,4,5]
def remove_dup(nums):
    i=0
    for j in range(len(nums)):
        if nums[j]!=nums[i]:
            i+=1
    return i
print(remove_dup(nums))
 