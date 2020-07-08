# 파이썬 딕셔너리가 해싱 테이블로 구현되어 있다길래 걍 딕셔너리 씀
import sys

n, m = map(int, input().split())
pw_dict = {}

for i in range(n):
    address, pw = sys.stdin.readline().strip().split()
    pw_dict[address] = pw

for i in range(m):
    key = sys.stdin.readline().strip()
    print(pw_dict[key])
