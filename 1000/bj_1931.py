import sys

n = int(input())
times = []
now_meeting_starts = last_meeting_ends = total = 0

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    times.append([end, start])

times = sorted(times)

for idx in range(n):
    if idx == 0:
        total += 1
        last_meeting_ends = times[idx][0]
        continue
    now_meeting_starts = times[idx][1]
    if last_meeting_ends <= now_meeting_starts:
        total += 1
        last_meeting_ends = times[idx][0]


print(total)
