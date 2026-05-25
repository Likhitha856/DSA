#find no.of set bits-------------------------
def count(n):
    count=0
    while(n>0):
        if n&1:
            count+=1
        n=n>>1
    return count
print(count(7))

#method 2 , removing rightmost set bit and increasing counter
def countSetBits(n):
    count = 0
    while n > 0:
        n = n & (n - 1) #n-1 changes rightmost set bit to 0 and then doing "&" will remove the rightmost set bit"
        count += 1      #n gets assigned to the binary num after eliminating the rightmmost set bit and continue the process, increment count
    return count
print(countSetBits(7))

#mehod 3, This expression isolates the rightmost set bit in n and minus from n to get perform same operation for n
def countSetBitsNest(n):
    count = 0
    while n > 0:
        n = n - (n & -n) #(n & -n)-This expression isolates the rightmost set bit in n and  n -(exp) to perform same operation agin
        count += 1
    return count