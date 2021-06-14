from collections import OrderedDict
def merge_the_tools(string,k):
    n=len(string)//k
    words=string.split("",n)

    for i in words:
        print("".join(OrderedDict.fromkeys(i)))

merge_the_tools('AABCAAADA',3)