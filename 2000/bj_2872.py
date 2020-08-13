import sys
input = sys.stdin.readline
n = int(input())
books = []

for i in range(n):
    tmp = int(input())
    books.append(tmp)

index = n
answer = 0

for i in range(n-1, -1, -1):
    if books[i] == index:
        index += 1
    else:
        answer += 1

print(answer)
