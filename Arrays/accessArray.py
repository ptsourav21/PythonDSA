from array import *

arr1 = array('i', [1,2,3,4,5,6])

def accessArray(array, index):
    if index>=len(array):           #time complexity O(1)
        print("Index out of bound") #time complexity O(1)
    else:
        print(array[index])         #time complexity O(1)

accessArray(arr1, 5)