n = int(input())
list2 = []
count = 0
list1 = []
for i in range(n):
    s = input()
    l = [el for el in s.split(" ")]

    if l[0]=='insert':
        list1.insert(int(l[1]),int(l[2]))

    if l[0]=='remove':
        list1.remove(int(l[1]))

    if l[0]=='append':
        list1.append(int(l[1]))

    if l[0]=='sort':
        list1.sort()

    if l[0]=='pop':
        list1.pop()

    if l[0]=='reverse':
        list1.reverse()

    if l[0]=='print':
        list2.append(list1[:])

for j in list2:
    print(j)