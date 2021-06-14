s=input()
l1=s.split(" ")
k=int(l1[0])
m=int(l1[1])
sum1=0

for i in range(k):
    s2=input()
    l2=s2.split(" ")
    maximum=int(max(l2))
    sum1+=maximum**2

print(sum1 % m)


