a=1242
b=276
def hcf(a,b):
    if a>b:
        a,b=b,a
    while a!=0:
        rem= b%a
        b,a=a,rem
        # b=a
        # a=rem
    return b
    
print(hcf(a,b))

#--------recursive-----#
def hcf(a,b):
    if a>b:
        a,b=b,a
    if a==0:
        return b
    rem=b%a
    b=a
    return(hcf(rem,b))

# result=hcf(a,b)
# print(result)


    