import sys
n=int(input())
phone_book=dict()
query_list=[]

for i in range(n):
    s=input()
    name_list=s.split(" ")
    phone_book[name_list[0]]=name_list[1]


query=input()
while query:
    phn_num=phone_book.get(query)
    if phn_num:
        print(query + '=' +phn_num)
    else:
        print('Not found')
    query = input()


