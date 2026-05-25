def diffps(num):
    prod=1
    sum=0
    while(num!=0):
        digit=num%10
        sum+=digit
        prod*=digit
        num=num//10
    diff=prod-sum
    return diff


def harshad(x):
    sum=0
    original=x
    while(x!=0):
        digit=x%10
        sum+=digit
        x=x//10

    harshad=original%sum
    print(harshad) 
    if harshad==0:
        return sum
    else:
        return -1
    
# print(harshad(23))

def countDigit(num):
    count=0
    while(num!=0):
        digit=num%10
        div=num%digit
        print(div)
        if div==0:
            count+=1
        num=num//10
    return count

# print(countDigit(1248))
def rev(num):
    rev=0
    while(num!=0):
        digit=num%10
        if digit!=0:
            rev=rev*10+digit
        num=num//10
    return rev

def conc(num):
    rev1=rev(num)
    while(num!=0):
        digit=num%10
        if digit!=0:
            sum+=digit
        num=num//10
    rev2=rev(rev1)
    return sum*rev1
# print(conc(10203004))

def conc2(num):
    same=0
    sum=0
    base=1
    while(num!=0):
        digit=num%10
        if digit!=0:
            same=same+base*digit
            base=base*10
            sum+=digit
        num=num//10
    print(sum,same)
    return same*sum 
# print(conc2(102030040))

import math
def pow(base,exp):
    pow=1
    for _ in range(exp):
        pow*=base
    return pow

def armstrong(num):
    length=int(math.log10(num)+1)
    original=num
    sum=0
    while(num!=0):
        digit=num%10
        p=pow(digit,length)
        sum+=p
        num=num//10
    return sum==original
# print(armstrong(1))

def gcd(a,b):
    if a>b:
        a,b=b,a
    while(a!=0):
        print(a,b)
        rem=b%a
        b=a
        a=rem
    return b
# print(gcd(9,18))
    
def rev(num):
    temp=num
    while(num!=0):
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev==temp 

