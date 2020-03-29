# 백준 2941번 크로아티아 알파벳
# 아이디어 : 리스트에 크로아티아 문자 저장 -> 그 문자를 ""로 replace

str1 = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for letter in croatia:
    str1 = str1.replace(letter, "1")

print(len(str1))
