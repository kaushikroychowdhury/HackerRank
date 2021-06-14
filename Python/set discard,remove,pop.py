n=int(input())
s=set(map(int,input().split(" ")))
k=int(input())
sum1=0

for i in range(k):
    list1=list(input().split(" "))

    if list1[0]=='pop':
        s.pop()

    if list1[0]=='remove':
        s.remove(int(list1[1]))

    if list1[0]=='discard':
        s.discard(int(list1[1]))

res_list=list(s)
for i in res_list:
    sum1+=i

print(sum1)