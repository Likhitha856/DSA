# import numpy as np

# arr=np.array([20,10,45,60,13,19,28])

# def bubbles(arr):
#     for i in range(0,len(arr)-1):
#         for j in range(0,len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# print(bubbles(arr))

import numpy as np

arr = np.array([20, 10, 45, 60, 13, 19, 28])

# def visual_bubble(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         print(f"\nPass {i + 1}:")
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             print(arr)  # Shows array after each comparison
#     return arr

# print("Visual Sort Result:", visual_bubble(arr))

#selection sort

# def selections(arr):
#     n=len(arr)
#     for i in range(n-1):
#         min_ind=i
#         for j in range(i+1,n):
#             if arr[min_ind]>arr[j]:
#                 min_ind=j
#         arr[i],arr[min_ind]=arr[min_ind],arr[i]
#         print(arr)
#     return f"final:{arr}"

# print(selections(arr))

#quick sort

def quicks(arr):
    if len(arr)<=1:
        return arr
    
    pivot=arr[0]
    left=[int(x )for x in arr[1:] if x<=pivot]
    right=[int(x) for x in arr[1:] if x>pivot]

    return np.array(list(quicks(left))+[pivot]+list(quicks(right)))

print(quicks(arr))
