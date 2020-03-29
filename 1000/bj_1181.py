import functools


def compare(str1, str2):
    if len(str1) > len(str2):  # 1
        return 1
    elif len(str1) < len(str2):
        return -1

    if str1 > str2:  # 2
        return 1
    else:
        return -1


n = int(input())
strList = []

for i in range(n):
    strList.append(input().rstrip())

strList = list(set(strList))  # 중복 제거
ansList = sorted(strList, key=functools.cmp_to_key(compare))  # 우선순위대로 정렬

for item in ansList:
    print(item)