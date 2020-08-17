import math

a, b, c = map(int, input().split())
x = 0

def binsearch(left, right):
    global ans
    while right - left > 10 ** -10:
        mid = (left + right) / 2.0
        print(mid)
        if a * mid + b * math.sin(mid) < c:
            left = mid
        else:
            right = mid
    ans = left

binsearch(0, 500001)
print(ans)
