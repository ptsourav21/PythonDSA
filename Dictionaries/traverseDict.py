myDict={'name':'Purnendu', 'age':26, 'address':'London'}

def traverseDict(dict):
    for key in dict: #..........................> O(N) space complexity O(1) because only traverse
        print(key, dict[key]) #.................> O(1)

traverseDict(myDict)