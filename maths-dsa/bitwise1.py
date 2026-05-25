# question 1

# def oddeven(n):
#     if n&1==1:
#         print("it is odd")
#     else:
#         print("it is even")

# oddeven(55)
#----------------------------------------
# question 2

# def  unique(arr):
#     uniq=0
#     for i in range(len(arr)):
#         uniq^=arr[i]

#     return uniq

# print(unique([2,3,4,6,4,3,2,6,5]))
#---------------------------------------
#question 3

# def sumToPositive(arr):
#     sum=0
#     for i in range(len(arr)):
#         sum+=arr[i]
    
#     print(sum)

# sumToPositive([2,-2,3,-3,5,6,-5,8,-8])
#---------------------------------------
#question 4

# def getpos(num,pos):
#     arr=[]
#     while(num>0):
#         rem=num%2
#         num=num//2
        
#         arr.append(rem)
#     print(arr)
#     return arr[pos]

# print(getpos(35,2))
#bitwise alt

# def getpos(num,pos):
#     return 1&(num>>pos)

# print(getpos(35,2))
#------------------------------------

# def getpos(num,n):
#     return num&(1<<(n-1))

# print(getpos(182,5))#16 where 10000 5th pos is 1 in 182(10110110) so it returns 16
#---------------------------------------
# question 5 set bit to 1
# def set_bit(num,pos):
#     return num|(1<<(pos-1))

# print(set_bit(86,4))
#-----------------------------------------