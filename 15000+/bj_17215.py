s = input()
score = 0

s = list(s.replace('-', '0'))

for i in range(len(s)):
    if s[i] == 'S':
        s[i] = '10'

i = 0
frame = 1
while frame < 11:
    if frame < 10:
        if s[i] == '10':  # strike
            score += 10
            if s[i+1] == '10':  # double
                score += 10 + int(s[i+2])
            elif s[i+2] == 'P':  # strike + spare
                score += 10
            else:
                score += int(s[i+1]) + int(s[i+2])
            i += 1
        elif s[i+1] == 'P':  # spare
            score += 10 + int(s[i+2])
            i += 2
        else:
            if s[i+1] == 'P':
                score += 10
            else:
                score += int(s[i]) + int(s[i+1])
            i += 2
    else:  # 10번째 프레임
        if s[i] == '10':
            if s[i+2] == 'P':
                score += 20
            else:
                score += 10 + int(s[i+1]) + int(s[i+2])
        elif s[i+1] == 'P':
            score += 10 + int(s[i+2])
        else:
            score += int(s[i]) + int(s[i+1])
    frame += 1


print(score)
