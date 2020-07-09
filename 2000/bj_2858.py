red, brown = map(int, input().split())

for i in range(1, red + brown + 1):
    if (red + brown) % i == 0:
        width = (red + brown) // i
        if width * 2 + i * 2 - 4 == red:
            if width > i:
                print(width, i)
            else:
                print(i, width)
            exit(0)
