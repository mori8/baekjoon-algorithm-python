num = int(input())

for i in range(num):
    str = input()
    sum = count = 0
    for answer in str:
        if answer is 'O':
            count += 1
            sum += count
        else :
            count = 0
    print(sum)