x, y, w, h = map(int, input().split())
lst = [x, y, h-y, w-x]
print(min(lst))