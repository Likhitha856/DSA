#a pow b TC=O(log(b))--------------------
def aPowb(a,b):
    if b==0 and a==0:
        return f"undefined 0^0"
    result=1
    #if b is negative
    if b<0:
        a=1/a
        b=-b
    while b>0:
        if b&1:
            result*=a
        b=b>>1       # TC is halved so it is log b, as it is running the digits time(binary 6=3 digits)
        a*=a
    return result
# print(aPowb(0,0))



