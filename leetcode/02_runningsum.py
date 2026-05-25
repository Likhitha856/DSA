nums=[1,2,3,4]
ans=[1,3,6,10]
def  running_sum(nums):
    sum=0
    runner=[]
    for i in range(len(nums)):
        sum+=nums[i]
        runner.append(sum)
    return runner
print(running_sum(nums))
