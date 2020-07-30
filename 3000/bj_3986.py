n = int(input())
cnt = 0
for i in range(n):
    string = input()
    if str(string) == str(string)[::-1]:
            cnt += 1

print(cnt)