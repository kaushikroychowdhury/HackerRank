n1=int(input())
s1=input()
list6=s1.split(" ")
a=set(list6)
#a.discard(' ')
n2=int(input())
s2=input()
list9=s2.split(" ")
b=set(list9)
#b.discard(' ')

a_list=list(a)
b_list=list(b)
list1=list(a.intersection(b))
merged_list = set(a_list + b_list)

for i in list1:
    merged_list.remove(i)

res_set=set(merged_list)
res_list=list(res_set)
res_list1=list(map(int,res_list))
res_list1.sort()

for j in res_list1:
    print(j)