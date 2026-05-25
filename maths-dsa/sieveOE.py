import numpy as np
from math import sqrt
n=int(input("enter num:"))

primes=np.zeros(n+1, dtype=bool)#size n+1 for inclusive else it will not be included as array starts from 0

def is_prime(n, primes):
    
    for i in range(2,int(sqrt(n)+1)):
        if not primes[i]:
            for j in range(i*i,n,i):
                primes[j]=True
                
    
    for i in range(2,n+1):#till n+1
        if not primes[i]:
            print(i, end=" ")

is_prime(n,primes)