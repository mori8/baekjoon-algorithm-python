for i in range(3):
    count = 0
    start, end = input().split()
    s = start.split(':')
    e = end.split(':')
    s = int(''.join(s))
    e = int(''.join(e))

    while s != e:
        if s % 3 == 0:
            count += 1
        s += 1
        if s % 100 == 60:
            s += 40
        if (s % 10000) // 100 == 60:
            s += 4000
        if s >= 240000:
            s %= 240000

    if s % 3 == 0:
        count += 1
    print(count)
