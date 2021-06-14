num=int(input())
str=input()
l=[int(el) for el in str.split(" ")]
s=sorted(set(l))
length = len(s)
print(s[length-2])

