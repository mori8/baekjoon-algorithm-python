# 백준 10867번 중복 빼고 정렬하기
# 아이디어 : 입력받는 list와 출력용 list를 따로 만들고 하나씩 옮긴다
# 옮기려는 숫자가 이미 출력용 list에 존재하면 옮기지 않는다

count = int(input())
nums = input().split()
ans = []

for num in nums:
    if int(num) not in ans:
        ans.append(int(num))

for i in sorted(ans):
    print(i, end=' ')
