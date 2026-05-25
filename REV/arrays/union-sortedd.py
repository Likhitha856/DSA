nums1=[1,3,4,6,8]
nums2=[1,3,4,5,9,18]
def union_sorted(nums1,nums2):
    arr=[]
    i=0
    j=0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]==nums2[j]:
            if not arr or arr[-1]!=nums1[i]:
                arr.append(nums1[i])
                i+=1
                j+=1
        elif(nums1[i]<nums2[j]):
            if not arr or arr[-1]!=nums1[i]:
                arr.append(nums1[i])
                i+=1
        else:
            if not arr or arr[-1]!=nums2[j]:
                arr.append(nums2[j])
                j+=1
    print(arr)
    while i<len(nums1):
        if not arr or arr[-1]!=nums1[i]:
            arr.append(nums1[i])
            i+=1
    while j<len(nums2):
        if not arr or arr[-1]!=nums2[j]:
            arr.append(nums2[j])
            j+=1
    return arr
print(union_sorted(nums1,nums2))
            