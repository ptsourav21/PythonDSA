myList=['a','b','c','d','e']
print(myList)
myList[0:2]=['x','y']
print(myList)

myList.pop()
print(myList)
myList.pop(0)
print(myList)

del myList[0:1]
print(myList)

myList.remove('d')
print(myList)