n, m = map(int, input().split())
cheap_natgae = cheap_6pack = 1001

for i in range(m):
    a, b = map(int, input().split())
    if a < cheap_6pack:
        cheap_6pack = a
    if b < cheap_natgae:
        cheap_natgae = b

if cheap_6pack < cheap_natgae * 6:
    money = min((n // 6) * cheap_6pack + (n % 6) * cheap_natgae, (n // 6 + 1) * cheap_6pack)
else:
    money = cheap_natgae * n
print(money)
