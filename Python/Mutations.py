string = input()
op = input()
l1=op.split(" ")
l2=list(string)
i = int(l1[0])
l2[i] = l1[1]
string = ''.join(l2)
print(string)