import sys

n, m = map(int, sys.stdin.readline().split())
index_dict = {}
name_dict = {}

for i in range(1, n+1):
    pokemon = sys.stdin.readline().strip()
    name_dict[i] = pokemon
    index_dict[pokemon] = i

for i in range(m):
    tmp = sys.stdin.readline().strip()
    if tmp.isdecimal():
        print(name_dict[int(tmp)])
    else:
        print(index_dict[tmp])
