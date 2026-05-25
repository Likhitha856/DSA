import math
def romanToInt( s: str) -> int:
    hashmap={'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000}
    sum=0
    
    count=0
    for i in s:
        count+=1
    original_count=count
    i=0
    j=i+1
    while(count>0):
        digit_i=hashmap[s[i]]
        new_digit=digit_i
        if i<(original_count-1):
            digit_j=hashmap[s[j]]
            print(digit_i,digit_j)

            if (s[i]=="I" and (s[j]=='V' or s[j]=='X')) or \
                (s[i]=="X" and (s[j]=='L' or s[j]=='C')) or \
                    (s[i]=="C" and (s[j]=='D' or s[j]=='M')):
                        new_digit=digit_j-digit_i
                        i+=1
                        count-=1
                        j+=1
        
        sum+=new_digit
        i+=1
        j+=1
        count-=1
        print(count)
            
    return sum

print(romanToInt("XCIXIX"))
