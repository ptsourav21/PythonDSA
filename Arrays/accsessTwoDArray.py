import numpy as np

a=np.array([[5,6,7,8],[10,11,12,13],[14,15,16,17]])
print(a)

b=np.insert(a,0,[[1,2,3,4]],axis=0)
print(b)

def accessElement(array, row, col):
    if row>=len(array) and col>=len(array[0]):
        print('Index Out of bound')
    else:
        print(array[row][col])

accessElement(b,2,3)