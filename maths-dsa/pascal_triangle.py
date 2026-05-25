import math as  m
#print pascal triangle------------------------------
def pascalT(n):
    triangle=[]
    for i in range(n+1):
        row=[1]*(i+1)
        for j in range(1,i): #1 to i-1 range
            row[j]=triangle[i-1][j-1]+triangle[i-1][j] #binomial expansion coefficients
            # print(row[j])
        triangle.append(row)
    return triangle
# print(pascalT(5))

#check if n is pow of 2 or not--------------------------------
def powOf2(n):
        if n==0:
             return False
        return n&(n-1)==0

print(powOf2(0))

#sum of nth row of pascal triangle is power of 2-------------------
def sumOfrow(n):
    triangle=pascalT(n)
    # print(triangle)
    for i in range(len(triangle)):
        # print(i)
        if n==i:
            return 1<<(n-1)
# sumOfrow(1)
# print(sumOfrow(5))