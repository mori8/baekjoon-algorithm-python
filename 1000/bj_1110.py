num = int(input())
new_num = -1
prev_num = num
count = 0

while num != new_num:
    tmp = (prev_num // 10) + (prev_num % 10)
    new_num = (prev_num % 10) * 10 + (tmp % 10)
    prev_num = new_num
    count += 1

print(count)