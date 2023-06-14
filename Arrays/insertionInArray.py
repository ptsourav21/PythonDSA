from array import *

arr1 = array('i',[1,2,3,4,5,6])
print(arr1)

#insert in first position
arr1.insert(0,0) # time complexity O(n)
print(arr1)

#insert in middle position
arr1.insert(3,1) #time complexity O(n)
print(arr1)

#insert in last position
arr1.insert(len(arr1),7) #time complexity O(1)
print(arr1)

