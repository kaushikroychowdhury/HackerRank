n=int(input())
list1=[]
for i in range(n):
    s=input()
    list1.append(s)

for j in range(n):
    s_odd = []
    s_even = []
    for i in range(len(list1[j])):
        if i%2==0:
            s_even.append(list1[j][i])
        else:
            s_odd.append(list1[j][i])

    print("".join(s_even)," ","".join(s_odd))