n = int(input())
string = input()
half = len(string) // 2 + (len(string) & 1)
str1 = list(string[:half])
str2 = list(string[half:])
cnt = 0

for i in range(2000):
    idx = len(string) // 2 - 1
    j = 1
    while idx >= 0:
        str1.insert(j, str2[idx])
        idx -= 1
        j += 2
    str2 = str1[half:]
    str1 = str1[:half]
    cnt += 1
    if str1 + str2 == list(string):
        break

period = cnt - n % cnt

for i in range(period):
    idx = len(string) // 2 - 1
    j = 1
    while idx >= 0:
        str1.insert(j, str2[idx])
        idx -= 1
        j += 2
    str2 = str1[half:]
    str1 = str1[:half]

print(''.join(str1 + str2))
