import sys
dic = {}
cnt = 0

for line in sys.stdin:
    if line == '\n':
        break
    r = line.rstrip()
    if dic.get(r):
        dic[r] += 1
    else:
        dic[r] = 1
    cnt += 1

sdict = sorted(dic.items())
for k, v in sdict:
    print("%s %.4f" % (k, v * 100 / cnt))
