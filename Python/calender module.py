import calendar
week_list=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
date=input()
list1=date.split(" ")
weekday=calendar.weekday(int(list1[2]),int(list1[0]),int(list1[1]))
print(week_list[weekday])
