def rotate180(num)->bool:
    rev=0
    original=num

    while(num>0):
        digit=num%10
        if digit==0:
            newdigit=0
        elif digit==1:
            newdigit=1
        elif digit==6:
            newdigit=9
        elif digit==8:
            newdigit=8
        elif digit==9:
            newdigit=6
        else:
            return False
        # if digit==2 or digit==3 or digit==4 or digit==5 or digit==7:
        #     return False 
        rev=10*rev+newdigit
        num=num//10 
    if rev==original:
        return True
    else:
        return False

test_cases = [
    0,
    1,
    8,
    6,
    9,
    69,
    96,
    101,
    818,
    619,
    689,
    8008,
    9861,
    6119,
    906,
    2,
    3,
    475,
    1289,
    9072
]


for i in test_cases:
    x=rotate180(i)
    print(x)


