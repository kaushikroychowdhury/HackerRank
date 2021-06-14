students=[[input(),float(input())] for _ in range(int(input()))]
marks_list =[]
for num in students:
    marks_list.append(num[1])

marks_list=sorted(set(marks_list))

name_list =[]

for i in students:
    if i[1] == marks_list[1]:
        name_list.append(i[0])

for name in sorted(name_list):
    print(name)

