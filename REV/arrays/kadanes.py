def max_subarray_sum(nums):
    if not nums:
        return 0,-1,-1
    max_sum=nums[0]
    sum=0
    start=0
    fstart=fend=0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum<0:
            sum=0
            start=i+1
        if sum>max_sum:
            max_sum=sum
            fstart=start
            fend=i
    return fstart,fend,max_sum
nums=[0,-2,-3,4,-1,-2,1,5,-8]
print(max_subarray_sum(nums))
#or check for negative returns
def kadane(nums):
    sum=0
    max_sum=nums[0]
    start=0
    fstart=fend=0
    for i in range(len(nums)):
        sum+=nums[i]
        if nums[i]>sum:
            sum=nums[i]
            start=i
        if sum>max_sum:
            max_sum=sum
            fstart=start
            fend=i
    return fstart,fend,max_sum
print(kadane(nums))
