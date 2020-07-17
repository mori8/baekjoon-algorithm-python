pan = input()
cases = 1

for i in range(len(pan)):
    if i != 0 and pan[i] == 'd' and pan[i] == pan[i-1]:
        cases *= 9
    elif i != 0 and pan[i] == 'c' and pan[i] == pan[i-1]:
        cases *= 25
    elif pan[i] == 'd':
        cases *= 10
    else:
        cases *= 26

print(cases)
