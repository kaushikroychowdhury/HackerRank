from collections import  deque
d=deque()
n=int(input())
for i in range(n):
    s=input()
    list1=s.split(" ")

    if list1[0]=='append':
        d.append(list1[1])

    elif list1[0]=='appendleft':
        d.appendleft(list1[1])

    elif list1[0]=='pop':
        d.pop()

    elif list1[0]=='popleft':
        d.popleft()

print(" ".join(d))