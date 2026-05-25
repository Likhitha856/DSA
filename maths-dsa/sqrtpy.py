n=40
high=n
low=0
p=3
def bs(high,low,p):
    root=0
    while(low<=high):
        mid=(high+low)//2
        if (mid*mid==n):
            root=mid
            return root
        elif mid*mid>n:
            high=mid-1
            root=mid
        else:
            low=mid+1
            root=mid #stores best guess so far
    inc=0.1
    for i in range(0,p+1):
        while root*root<n:
            root+=inc
        root-=inc
        inc=inc/10
    return round(root,p)

print(bs(high,low,p))



