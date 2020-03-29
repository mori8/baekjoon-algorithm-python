n = int(input())
sixList = []
count = 0

for i in range(2670000):
    if "666" in str(i):
        sixList.append(i)

print(sixList[n-1])