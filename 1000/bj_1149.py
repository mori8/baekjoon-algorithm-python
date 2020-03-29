# dynamic programing
# 점화식 : i번째 집을 칠하는 비용 + i 번째에 칠한 색을 제외한 색을 i-1번째에 칠하는 비용
# 맨 끝에서부터 보면 경우의 수가 3가지. 마지막 집을 빨강/초록/파랑으로 칠하는 경우
# 따라서 집을 칠하는 비용의 최소값은 위 3가지 경우 중 값이 가장 최소인 경우의 값임.

num_of_house = int(input())

cost_list = []  # index 0:red, 1:green, 2:blue
cost_sumlist = [[0]*3 for x in range(num_of_house)]

for n in range(num_of_house):
    r, g, b = map(int, input().split())
    cost_list.append([r, g, b])

for i in range(num_of_house):
    if i == 0:
        cost_sumlist[0] = cost_list[0]
    else:
        cost_sumlist[i][0] = cost_list[i][0] + min(cost_sumlist[i-1][1], cost_sumlist[i-1][2])  # R
        cost_sumlist[i][1] = cost_list[i][1] + min(cost_sumlist[i-1][0], cost_sumlist[i-1][2])  # G
        cost_sumlist[i][2] = cost_list[i][2] + min(cost_sumlist[i-1][0], cost_sumlist[i-1][1])  # B

print(min(cost_sumlist[-1]))

