import functools


def intsum(string):
    sum = 0
    for i in string:
        if 48 <= ord(i) <= 57:
            sum += int(i)
    return sum


def compare(str1, str2):
    if len(str1) > len(str2):  # 첫번째 조건
        return 1
    elif len(str1) < len(str2):
        return -1

    strint1 = intsum(str1)
    strint2 = intsum(str2)

    if strint1 > strint2:  # 두번째 조건
        return 1
    elif strint1 < strint2:
        return -1

    if str1 > str2:  # 세번째 조건
        return 1
    else:
        return -1


n = int(input())
strList = []

for i in range(n):
    str = input()
    strList.append(str)

ansList = sorted(strList, key=functools.cmp_to_key(compare))

for item in ansList:
    print(item)