def any_isalnum(string):
     l = list(string)
     l1 = []
     count = 0
     for i in l:
         b=i.isalnum()
         l1.append(b)

     for j in l1:
         if j is True:
             count += 1
     if count != 0:
         return True
     return False


def any_isalpha(string):
    l = list(string)
    l1 = []
    count = 0
    for i in l:
        b = i.isalpha()
        l1.append(b)

    for j in l1:
        if j is True:
            count += 1
    if count != 0:
        return True
    return False


def any_isdigit(string):
    l = list(string)
    l1 = []
    count = 0
    for i in l:
        b = i.isdigit()
        l1.append(b)

    for j in l1:
        if j is True:
            count += 1
    if count != 0:
        return True
    return False


def any_islower(string):
    l = list(string)
    l1 = []
    count = 0
    for i in l:
        b = i.islower()
        l1.append(b)

    for j in l1:
        if j is True:
            count += 1
    if count != 0:
        return True
    return False


def any_isupper(string):
    l = list(string)
    l1 = []
    count = 0
    for i in l:
        b = i.isupper()
        l1.append(b)

    for j in l1:
        if j is True:
            count += 1
    if count != 0:
        return True
    return False

s=input()
print(any_isalnum(s))
print(any_isalpha(s))
print(any_isdigit(s))
print(any_islower(s))
print(any_isupper(s))
