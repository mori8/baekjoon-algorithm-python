num = int(input())

for i in range(num):
    number, string = input().split()
    txt = ''
    for j in string:
        txt += j * int(number)
    print(txt)