# 백준 10809번 알파벳 찾기
# 아이디어 : -1을 보자마자 떠올랐다 find()

import string

str1 = input()
ansDict = []
i = 0

for alpha in string.ascii_lowercase:
    ansDict.append(str1.find(alpha))
    i += 1

for i in ansDict:
    print(i, end=' ')