from array import *

arr1=array('i', [1,2,3,4,5,6])

def searchInArray(arr1, value):
    for i in arr1:
        if i==value:
            return arr1.index(value)
    return "This value is not in array"
#time complexity of this function is O(n)

print(searchInArray(arr1,5))