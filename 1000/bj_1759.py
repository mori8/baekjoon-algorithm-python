from itertools import combinations

l, c = map(int, input().split())
letters = sorted(input().split())
vowels = {'a', 'e', 'i', 'o', 'u'}
comb = list(combinations(letters, l))

for x in comb:
    test = vowels & set(x)
    if len(test) >= 1 and len(x) - len(test) >= 2:
        print(''.join(x))
