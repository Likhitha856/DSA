import math
#---------------FACTORS-1-----TC=O(n)---------#
n=20
def factors1(n):
    for i in range(1,n+1):
        if n % i==0:
            print(i, end=" ")
# factors1(n)

#---------------FACTORS_2------TC=O(sqrt(n))--#

def factors2(n):
    for i in range(1,int(math.sqrt(n))+1):
        if n % i==0:
            if n/i==i:
                print(i, end=" ")
            else:
                print(i,end=" ")
                print(int(n/i), end=" ")
# factors2(n)

#-------------FACTORS-3-----TC=O(sqrt(n)),SC=O(sqrt(n))---------#
arr=[]
def factors3(n):
    for i in range(1,int(math.sqrt(n))+1):
        if n % i ==0:
            if n / i==i:
                print(i, end=" ")
            else:
                print(i,  end=" ")
                j=n/i
                arr.append(int(j))
    
    s=len(arr)-1
    for i in range(s,-1,-1):
        print(arr[i], end=" ")
     
factors3(n)