from itertools import combinations_with_replacement
s=input()
list1=s.split(" ")
k=int(list1[1])
string=list1[0]
list2=[]
res_list=[]
m=[]

list2.append(list(combinations_with_replacement(string,k)))
#list2.remove(list2[0])

for j in list2:
    for l in j:
        m=list(l)
        m.sort()
        res_list.append(''.join(m))

res_list.sort()
res_list.sort(key=len,reverse=False)
for k in res_list:
    print(k)
