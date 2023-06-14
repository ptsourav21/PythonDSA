# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
s= set(map(int, input().split()))
m= int(input())
command=[]
for i in range(m):
    list1=input().split()
    command.append(list1)
for i in command:
    if i[0]=='pop':
        s.pop()
    elif i[0]=='remove':
        s.remove(int(i[1]))
    elif i[0]=='discard':
        s.discard(int(i[1]))
print(sum(s))
    
