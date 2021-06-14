n=int(input())
list2=[]
for i in range(n):
    s = input()
    list1 = s.split(" ")

    try:
        int(list1[0])//int(list1[1])
    except ZeroDivisionError as e:
        if ZeroDivisionError:
            list2.append("Error Code: "+ str(e))

    except ValueError as e:
        if ValueError:
            list2.append("Error Code: "+str(e))
    else:
        list2.append(int(list1[0]) // int(list1[1]))


for i in list2:
    print(i)