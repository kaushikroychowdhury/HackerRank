from itertools import product
A=input()
B=input()
list1=[]
list2=[]
list_result=[]
a_list=A.split(" ")
b_list=B.split(" ")
for i in a_list:
    list1.append(int(i))
for j in b_list:
    list2.append(int(j))

list_result=list(product(list1,list2))
for k in list_result:
    print(k , end=" ")
