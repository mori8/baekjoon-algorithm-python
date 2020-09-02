import sys
import math
input = sys.stdin.readline
n = int(input())
x = []
y = []
z = []
sumx = 0
sumy = 0
sumz = 0
dis = 0


def dist(c, d, e):
    return c * c + d * d + e * e


for i in range(n):
    a, b, c = map(int, input().rstrip().split())
    x.append(a)
    y.append(b)
    z.append(c)
    sumx += a
    sumy += b
    sumz += c

sumx /= n
sumy /= n
sumz /= n
g = 0.1

for i in range(50000):
    f = 0
    dis = dist(sumx - x[0], sumy - y[0], sumz - z[0])
    for j in range(1, n):
        tmp = dist(sumx - x[j], sumy - y[j], sumz - z[j])
        if dis < tmp:
            dis = tmp
            f = j
    sumx += (x[f] - sumx) * g
    sumy += (y[f] - sumy) * g
    sumz += (z[f] - sumz) * g
    g *= 0.998

print("%.2f" % round(math.sqrt(dis), 2))
