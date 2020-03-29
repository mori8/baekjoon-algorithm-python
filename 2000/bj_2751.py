count = int(input())
lst = []

for i in range(count):
    lst.append(int(input()))

for j in sorted(lst):
    print(j)