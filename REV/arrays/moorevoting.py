def majorityel(nums):
    count=0
    maj_el=None
    for i in range(len(nums)):
        if count==0:
            maj_el=nums[i]
        elif maj_el==nums[i]:
            count+=1
        else:
            count-=1
    c=0
    for i in range(len(nums)):
        if nums[i]==maj_el:
            c+=1
    if c>len(nums) // 2:
        return maj_el
    else:
        return None
nums=[7,7,7,7,7,3,4,5,7,8,9,0,7,7,7,7,6,7,7]
print(majorityel(nums))