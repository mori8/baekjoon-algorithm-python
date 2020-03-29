# 백준 14717번 앉았다
# 아이디어 : a나 b를 포함하는 경우 + 둘 다 포함하지 않는 경우 따로 확률 계산 후 더하기

a, b = map(int, input().split())

Set = []

includeABSet = []
noIncludeABSet = []

for i in range(1, 11) :
    for j in range(i, 11) :
        if i != j and (i + j) % 10 < (a + b) % 10:
            Set.append([i, j])

if a == b:
    print("%.3f" % (1 - (10 - a)/153))

else :
    for l in Set:
        if (a == l[0] or b == l[1]) or (b == l[0] or a == l[1]):
            includeABSet.append(l)
        else :
            noIncludeABSet.append(l)
    print("%.3f" % ((2 * len(includeABSet) + 4 * len(noIncludeABSet)) / 153))
