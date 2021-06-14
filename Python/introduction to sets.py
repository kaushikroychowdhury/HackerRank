def average(array):
    set1 = set(array)
    l = len(set1)
    sum1 = 0
    for i in set1:
        sum1 += int(i)

    return sum1 / l


