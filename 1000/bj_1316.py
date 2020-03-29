# 백준 1316번 그룹 단어 체커
# 아이디어 : 인덱스 슬라이싱 이용 제일 첫번째로 나온 x의 인덱스와 제일 나중에 나온 x의 인덱스 사이에 x가 아닌 단어가 존재하면 그룹 단어 아님

count = int(input())
num = 0

for i in range(count):
    str1 = input()
    for j in str1:
        flag = True
        for letter in str1[str1.find(j)+1: str1.rfind(j)]:
            if letter is not j:
                flag = False
                break
                print(j, letter)
                print(str1[str1.find(j)+1: str1.rfind(j)])
            # elif letter in str1[:str1.find(j)]:
            #     flag = False
        if not flag:
            break
    if flag:
        num += 1
print(num)

# N = int(input())
# countGroupNum = 0
# for j in range(N):
#     getStr = input()
#
#     if len(getStr) == 1:
#         countGroupNum += 1
#
#     for i in range(len(getStr) - 1):
#         if getStr[i] != getStr[i + 1]:
#             if getStr[i] in getStr[i + 1:]:
#                 break
#
#         if i == len(getStr) - 2:
#             countGroupNum += 1
#
# print(countGroupNum)