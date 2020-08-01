import math

def preprocessing(num):
    k = int(math.log10(num))
    size = 0
    for i in range(k):
        size += (10 ** (i + 1) - 10 ** i) * (i + 1)
    size += (num - 10 ** k + 1) * (k + 1)
    return size


# def bsearch(left, right):
#     while left < right:
#         mid = (left + right) // 2
#         print("mid:", mid)
#         tmp = preprocessing(mid)
#         print("tmp:", tmp)
#         if tmp < k:
#             left = mid + 1
#         else: right = mid
#     return right

def bsearch(left, right):
    while left < right:
        mid = (left + right) // 2
        print(mid)
        tmp = preprocessing(mid)
        print(tmp)
        if tmp < k:
            left = mid + 1
        elif tmp > k:
            right = mid
        else:
            break
    return mid



n, k = map(int, input().split())
num = bsearch(1, n)
print(num)
size = preprocessing(num)
print(size)
if size < k:
    print(-1)
else:
    print(str(num)[len(str(num)) - (size - k) - 1])