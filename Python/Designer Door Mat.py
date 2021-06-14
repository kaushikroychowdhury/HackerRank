s=input()
l=s.split(" ")
n=int(l[0])
m=int(l[1])

c='.|.'

row=n//2
for i in range(1,row*2):
    if i%2 != 0:
        print((c*i).center(m,'-'))

print('WELCOME'.center(m,'-'))

for j in range((row*2)-1,0,-2):
    print((c*j).center(m,'-'))