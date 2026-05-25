a=234
b=91

def hcf(a,b):
    if a>b:
        a,b=b,a
    while a!=0:
        rem= b%a
        b,a=a,rem
        # b=a
        # a=rem
    return b
#------------------------------#
# def lcm(x,y):
#     if x>y:
#         x,y=y,x
#     a=x
#     b=y
#     while a!=0:
#         rem= b%a
#         b=a
#         a=rem
#     f=x/b
#     g=y/b
#     return int(f*g*b)

# result=lcm(a,b)
# print(result)
#---------------------------------#
def lcm(a,b):
    d=hcf(a,b)
    return (a*b)/d

print(lcm(a,b))