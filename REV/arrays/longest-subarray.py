# with garget using optimal sliding window approach
nums = [10, 5, 2, 7, 1, 9]
target=15
def longest_subarray(nums,target):
    i=0
    start=0
    # curr=0
    # end=0
    sum=0
    max_count=0
    for i in range(len(nums)):
        sum+=nums[i]
        while sum>target:
            sum-=nums[start]
            start+=1
        if target==sum:
            max_count=max(max_count,(i-start+1))
    return max_count
print(longest_subarray(nums,target))
#prefix-sum technique

def longest_sub(nums,target):
    hashmap={0:-1}
    prefix_sum=0
    maxl=0
    start=end=-1
    # start and end are never assigned
    # They don’t exist
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        if (prefix_sum-target) in hashmap:
            length=i-hashmap[prefix_sum-target]
            if length>maxl:
                maxl=length
                start=hashmap[prefix_sum-target]+1
                end=i
        if prefix_sum not in hashmap:
            hashmap[prefix_sum]=i