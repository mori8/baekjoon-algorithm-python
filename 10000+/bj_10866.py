# 백준 10866번 덱
import sys


class Deque:
    def __init__(self):
        self.data = []

    def push_front(self, item):
        self.data.insert(0, item)

    def push_back(self, item):
        self.data.append(item)

    def pop_front(self):
        if len(self.data) == 0:
            return -1
        tmp = self.data[0]
        del self.data[0]
        return tmp

    def pop_back(self):
        if len(self.data) == 0:
            return -1
        return self.data.pop()

    def size(self):
        return len(self.data)

    def empty(self):
        if len(self.data) == 0:
            return 1
        return 0

    def front(self):
        if len(self.data) == 0:
            return -1
        return self.data[0]

    def back(self):
        if len(self.data) == 0:
            return -1
        return self.data[-1]


n = int(input())
d = Deque()

for x in sys.stdin:
    cmd = x.split()
    if cmd[0] == "push_back":
        d.push_back(int(cmd[1]))
    elif cmd[0] == "push_front":
        d.push_front(int(cmd[1]))
    elif cmd[0] == "front":
        print(d.front())
    elif cmd[0] == "back":
        print(d.back())
    elif cmd[0] == "size":
        print(d.size())
    elif cmd[0] == "empty":
        print(d.empty())
    elif cmd[0] == "pop_front":
        print(d.pop_front())
    elif cmd[0] == "pop_back":
        print(d.pop_back())

