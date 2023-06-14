myList=[1,2,3,4,5,6]
if 3 in myList:
    print(myList.index(3))

def searchList(list, value):
    for i in list:
        if i==value:
            return list.index(i)+1
    return "The value does not exist"

print(searchList(myList,3))

