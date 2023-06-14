from array import *

arr1= array('i',[0,1,2,3,4,5,6])
print(arr1)
# Time complexity of removing first element is O(n)
arr1.remove(1) 
print(arr1)
# Time complexity of removing middle element is O(n)
arr1.remove(4)
print(arr1)
# Time complexity of removing last element is O(1)
arr1.remove(6)
print(arr1)