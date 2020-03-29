# 백준 15565번 귀여운 라이언
# 아이디어 : 1이 몇번째 index에 있는지 탐색하고 리스트에 저장
#          list[i + (num - 1)] - list[i]]의 값이 가장 작은 경우를 minimum에 저장한 후 출력

length, num = map(int, input().split())

friends = []
lions = []
friends = input().split()

minimum = length

for i in range(length):
    if int(friends[i]) is 1:
        lions.append(i)

if not lions or len(lions) < num:
    print(-1)
else:
    for i in range(len(lions) - (num - 1)):
        if (lions[i + (num - 1)] - lions[i] + 1) < minimum:
            minimum = lions[i + (num - 1)] - lions[i] + 1

    print(minimum)