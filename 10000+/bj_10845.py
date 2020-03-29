class Queue:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.insert(0, item)

    def isEmpty(self):
        if len(self.data) == 0:
            return 1
        return 0

    def size(self):
        return len(self.data)

    def pop(self):
        if self.isEmpty() == 1:
            return -1
        return self.data.pop()

    def front(self):
        if self.isEmpty() == 1:
            return -1
        return self.data[-1]

    def back(self):
        if self.isEmpty() == 1:
            return -1
        return self.data[0]


# main
import sys

n = int(input())
q = Queue()

for x in sys.stdin:
    tmp = x.split()
    if tmp[0] == "push":
        q.push(tmp[1])
    if tmp[0] == "front":
        print(q.front())
    if tmp[0] == "back":
        print(q.back())
    if tmp[0] == "size":
        print(q.size())
    if tmp[0] == "empty":
        print(q.isEmpty())
    if tmp[0] == "pop":
        print(q.pop())