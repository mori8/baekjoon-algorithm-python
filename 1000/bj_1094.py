count = 0
num = int(input())
bi = format(num, 'b')
for x in bi:
    if x == '1': count += 1
print(count)