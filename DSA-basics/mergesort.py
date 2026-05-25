nums=[2,5,1,8,3,2]
# l=first index u=last index
# stops when l==u
def m_sort(arr,l,u):
    if l<u:
        mid=(l+u)//2
        m_sort(arr,l,mid)
        m_sort(arr,mid+1,u)
        merge(arr,l,mid,u)
    return arr
    
def merge(arr,l,mid,u):
    left=arr[l:mid+1]
    # include last element
    right=arr[mid+1:u+1]
    i=0
    j=0
    k=l
    # two pointers start at each array
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        k+=1
        i+=1
    while j<len(right):
        arr[k]=right[j]
        k+=1
        j+=1


# print(m_sort(nums,0,len(nums)-1))
# -------------------

def ms(arr,l,u):
    if l<u:
        mid=(l+u)//2
        ms(arr,l,mid)
        ms(arr,mid+1,u)
        m(arr,l,mid,u)
    return arr

def m(arr,l,mid,u):
    left=arr[l:mid+1]
    right=arr[mid+1:u+1]
    i=j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        k+=1
        i+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
# print(ms(nums,0,len(nums)-1))


# ------------------------------------

def s1(arr,l,u):
    if l<u:
        mid=(l+u)//2
        s1(arr,l,mid)
        s1(arr,mid+1,u)
        m1(arr,l,mid,u)
    return arr
def m1(arr,l,mid,u):
    left=arr[l:mid+1]
    right=arr[mid+1:u+1]
    i=j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        k+=1
        i+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
print(s1(nums,0,len(nums)-1))
            
            
