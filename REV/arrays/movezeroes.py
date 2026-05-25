def movetoend(nums):
    AZeroPos=0 #last(previous)zero pos with which i switched non zero el
    for current in range(len(nums)):
        if nums[current]!=0:
            nums[current],nums[AZeroPos]=nums[AZeroPos],nums[current]
            AZeroPos+=1
    return nums
nums=[0,1,2,0,0,3,0]
print(movetoend(nums))