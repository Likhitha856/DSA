import math as m
def count(n,base):
    return int(m.log(n)/m.log(base)) +1

# print(count(10,10))   

def shiftcount(n): #only binary
    count=0
    while(n>0):
        n=n>>1
        count+=1
    return count
print(shiftcount(10))