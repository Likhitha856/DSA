nums = [2, 4, 5, -1, -3, -4]
def altsigned(nums):
    pos=neg=0
    for i in range(0,len(nums),2):
        print(i)
        if nums[i]<0:
            for j in range(i,len(nums)):
                if nums[j]>0:
                    new=j
                    break
            nums[i],nums[new]=nums[new],nums[i]
        if nums[i+1]>0:
            for j in range(i,len(nums)):
                if nums[j]<0:
                    new=j
                    break
            nums[i+1],nums[new]=nums[new],nums[i+1]
    return nums
print(altsigned(nums))