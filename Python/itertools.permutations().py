from itertools import permutations
s=input()
n=s.split(" ")
k=int(n[1])
s_list=[i for i in n[0]]
result_list=list(permutations(s_list,k))
result1=[]

for i in result_list:
    result1.append("".join(i))

result1.sort()
for j in result1:
    print(j)