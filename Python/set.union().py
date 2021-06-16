n1=int(input())
st1=set(map(int,input().split(" ")))
n2=int(input())
st2=set(map(int,input().split(" ")))

count=0
res_set=st1.union(st2)
for i in res_set:
    count+=1

print(count)