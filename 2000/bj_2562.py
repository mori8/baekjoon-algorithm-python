lst = []
for i in range(9):
    lst.append(int(input()))
print(sorted(lst)[-1])
print(lst.index(sorted(lst)[-1]) + 1)