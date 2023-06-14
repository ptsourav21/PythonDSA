#Linear Search

myDict={'name':'Purnendu', 'age':26, 'address':'London'}

def searchDict(dict, value):
    for key in dict: #..........................> O(N)
        if dict[key]==value:  #.................> O(1)
            return key, value #.................> O(1)
    return 'the value does not exist'

print(searchDict(myDict, 26))