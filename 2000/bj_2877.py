n = int(input())
s = format(n+1, 'b')
i = s.index('1')
s = s[i+1:]
for x in s:
    if x == '0':
        print('4', end='')
    else:
        print('7', end='')
