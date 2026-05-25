def happy_number(num):
    sum=0
    temp=num
    lis=[]
    while(sum!=1):
        sum=0
        while( num !=0 ):
            digit=num % 10
            sum+=digit**2
            num=num//10
            
        num=sum
        print(num)
        if lis and sum in lis:
            return False
        lis.append(sum)     
        if(sum == 1):
            return True
                  
    return False
print(happy_number(986543210))

# optimized 
# If the sequence enters a cycle, a faster pointer that moves two steps per iteration 
# will eventually catch the slower pointer (same principle as detecting cycle in a linked list).