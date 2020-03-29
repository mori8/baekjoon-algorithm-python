# 백준 1427번 단어 공부
# 아이디어 : str로 입력받고 바로 sort()

num = input()

for i in sorted(num, reverse=True):
    print(i, end='')

