sum=0
n=int(input())
student_marks = {}
name =str()
score = []
for _ in range(n):
    line = input().split()
    name , score = line[0] , line[1:]
    student_marks[name] = score

res_name = input()
marks = student_marks.get(res_name)
for i in marks:
    sum+=float(i)

avg = sum/3
output = round(avg,2)
print("%.2f" % output)
