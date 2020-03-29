lst = list(map(int, input().split()))
if lst == sorted(lst):
    print("ascending")
elif lst == sorted(lst, reverse=True):
    print("descending")
else:
    print("mixed")