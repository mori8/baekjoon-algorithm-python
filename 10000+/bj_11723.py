import sys
n = int(input())
s = [False] * 21

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:
        arg = int(cmd[1])
    if cmd[0] == 'add':
        s[arg] = True
    elif cmd[0] == 'check':
        if s[arg]:
            print('1')
        else:
            print('0')
    elif cmd[0] == 'remove':
        s[arg] = False
    elif cmd[0] == 'toggle':
        if s[arg]:
            s[arg] = False
        else:
            s[arg] = True
    elif cmd[0] == 'all':
        s = [True] * 21
    elif cmd[0] == 'empty':
        s = [False] * 21
