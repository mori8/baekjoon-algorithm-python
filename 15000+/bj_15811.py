from itertools import permutations
import sys


nums = [x for x in range(10)]
op1, op2, ans = map(list, sys.stdin.readline().split())


def solve():
    fir = sec = thi = 0
    for i in op1:
        fir *= 10
        fir += alnumDict[i]
    for i in op2:
        sec *= 10
        sec += alnumDict[i]
    for i in ans:
        thi *= 10
        thi += alnumDict[i]
    return thi == fir + sec


alphaList = sorted(list(set(op1 + op2 + ans)))

alnumDict = {}
alphaLength = len(alphaList)

for k in permutations(nums, alphaLength):
    if alphaLength > 10:
        break
    for i in range(alphaLength):
        alnumDict[alphaList[i]] = k[i]

    if solve():
        print("YES")
        exit(0)

print("NO")
