#xor all number from 0 to a
def xor(a):
    if a%4==0:
        return a
    elif a%4==1:
        return 1
    elif a%4==2:
        return a+1
    elif a%4==3:
        return 0
# print(xor(9))

#xor numbers btwn a and b
def xor2(a,b):
    x=xor(b)
    y=xor(a-1)
    return x^y
print(xor2(9,20))