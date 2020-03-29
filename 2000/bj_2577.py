# 백준 2577번 숫자의 개수
# 아이디어 : a * b * c 의 값을 str로 변환 -> for로 탐색

a = int(input())
b = int(input())
c = int(input())

number = str(a * b * c)

ans_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in number:
    ans_arr[int(i)] += 1

for num in ans_arr:
    print(num)
