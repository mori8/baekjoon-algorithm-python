string = input()
poly = []
tmp = ''
answer = 0
isMinus = False

for x in string:
    if x == '-' or x == '+':
        poly.append(tmp)
        poly.append(x)
        tmp = ''
    else:
        tmp += x
poly.append(tmp)

for i in range(len(poly)):
    if poly[i].isdigit() and not isMinus:
        if i == 0 or poly[i-1] == '+':
            answer += int(poly[i])
        else:
            answer -= int(poly[i])
    elif poly[i].isdigit() and isMinus:
        answer -= int(poly[i])
    elif poly[i] == '-':
            isMinus = True

print(answer)
