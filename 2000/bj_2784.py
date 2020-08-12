import sys
from itertools import permutations

words = []
for line in sys.stdin:
    words.append(line.strip('\n'))

for x in permutations(words, 6):
    if x[0][0] + x[1][0] + x[2][0] == x[3]:
        if x[0][1] + x[1][1] + x[2][1] == x[4]:
            if x[0][2] + x[1][2] + x[2][2] == x[5]:
                print(x[0])
                print(x[1])
                print(x[2])
                exit(0)

print("0")