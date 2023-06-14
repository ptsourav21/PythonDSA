import numpy as np

a=np.array([[5,6,7,8],[10,11,12,13],[14,15,16,17]])
print(a)

b=np.insert(a,0,[[1,2,3,4]],axis=0)
print(b)

def traverseArray(array):
    for i in range(len(array)):       
        for j in range(len(array[0])):
            print(array[i][j])
# on 10th line time complexity is O(mn)
# on 11th line time complexity is O(n)
# on 12th line time complexity is O(1)
# space complexity is always O(1)
traverseArray(b)