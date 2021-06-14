s=input()
l=list(s.split(" "))
n=len(l)
li=[l[i].capitalize() for i in range(n)]
print(" ".join(li))