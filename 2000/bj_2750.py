# 백준 2750, 2751번 수 정렬하기 1, 2
# 아이디어 : sorted() 사용

count = int(input())
lst = []

for i in range(count):
    temp = int(input())
    lst.append(temp)

for j in sorted(lst, reverse=True):
    print(j)