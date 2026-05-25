import array as a
import numpy as np
fruits=np.array([1,2,3,"orange",'banana',"apple"]) #type coercion changes all to strings
nums=a.array('i',[1,2,3])#doesn't support strings
# print(fruits)
# for i in range(len(nums)):
#     print(nums[i])
#---------------------------------------------python arrays-------------------------------------------#
x=list(range(0,20,2))
even20=a.array('i',x)
# print(even20[2])

#adding element
even20.insert(6,12)
# print(even20)

#appending 
even20.append(20)
# print(even20)

#updating
even20[7]=14
# print(even20)

#popping/deleting
even20.pop(7)#index
even20.remove(10)#element
# print(even20)

even10=even20[0:6]#last index exclusive 
# print(even10)
# print(even20)

#slicing
# even10=even20[::-1]
# print(even10)

#searching
index=even10.index(6)#search element should pe passed
key=even10[index]
# print(index,key)

#sorting---arr.sort() doesn't work
arr=a.array('i',[8,9,5,6,3])
new=sorted(arr)
# print(new)

#---------------------------------------------numpy arrays-----------------------------------#
ar=np.array([6,3,7,9,10])

const=np.full((2,2),5)
# print(const)
ones=np.ones((3,3),dtype=int)#creates floating point initially
# print(ones)
zeros=np.zeros(5, dtype=bool) 
# print(zeros)

#identity matrix
iden=np.eye(2, dtype=int)
# print(iden)

#random matrix
r=np.random.randint(10,20,size=(2,3)) #dtpe must be integer float not allowed
# print(r)
# print(type(r)) #array type

#2-d array
twod=np.array([[5,6,],[4,5]])
# print(twod)

fived=np.array([5,6,7,8], ndmin=5)
# print(fived)

#deleting
new_ar=np.delete(ar,3) #give array and index to be deleted
# print(new_ar)

#searching
index=np.where(ar==7)
# print(index)

#sorting
ar2=np.sort(ar)
print(ar2)

#math opr add and sub 2 arrays
add=np.add(ar,ar2)       #2 arrays should be of the same size for add and sub
sub=np.subtract(ar,ar2)
print(add,sub)
