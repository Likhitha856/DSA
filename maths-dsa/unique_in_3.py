def unique(nums):
    result=0
    for i in range (32):
        bit_sum=0
        for num in nums:    #for all numbers in nums
            if (num>>i)&1:  #one position wise(ith)
                bit_sum+=1  #calculate bit_sum
        if bit_sum%3 != 0:  #check if that bit_sum for that ith postiion for all numbers is div by 3, if not then that is the set bi of uniq num, so keep that in result
            result=result|(1<<i) #left shifting 1 to that bits a position is to set ith bit to 1, and recursively doing or 
                                 #with the "result" preserves prev result bit
    if result>=2**31:         #for negative numbers, 2**31 = 2147483648 → the first number that doesn't fit in positive range(4294967246 >= 2147483648 → True)
        result-=2**32         #Convert the unsigned interpretation to signed 2’s complement( result = 4294967246 - 4294967296 = -50)
    return result
print(unique([2,2,2,3,3,3,-70,5,5,5,6,6,6]))