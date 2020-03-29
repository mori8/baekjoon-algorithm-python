# 백준 11656번 접미사 배열
# 아이디어 : 리스트 인덱스 슬라이싱

str1 = input()
lst = []

for i in range(len(str1)):
    lst.append(str1)
    str1 = str1[1:]

for i in sorted(lst):
    print(i)