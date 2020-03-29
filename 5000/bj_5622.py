# 백준 5622번 다이얼
# 아이디어 : 리스트 인덱스 이용

str1 = input()
time = 0

alphas = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for letter in str1:
    for alpha in alphas:
        if letter in alpha:
            time += alphas.index(alpha) + 3
            print(time)
            break

print(time)