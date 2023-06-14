from array import *

arr1 = array('i',[1,2,3,4,5,6])
print(arr1)

def traverseArray(arr):
    for i in arr: #time complexity O(n)
        print(i)  #time complexity O(1)
                  #total complexity O(n)
traverseArray(arr1)