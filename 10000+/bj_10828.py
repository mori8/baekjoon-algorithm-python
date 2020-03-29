# 백준 10828번 스택
import sys

class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        if self.size() == 0:
            return 1
        return 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.isEmpty() == 1:
            return -1
        return self.data.pop()

    def top(self):
        if self.isEmpty() == 1:
            return -1
        return self.data[-1]


# main

n = int(input())
s = Stack()

for x in sys.stdin:
    tmp = x.split()
    if tmp[0] == "push":
        s.push(tmp[1])
    if tmp[0] == "top":
        print(s.top())
    if tmp[0] == "size":
        print(s.size())
    if tmp[0] == "empty":
        print(s.isEmpty())
    if tmp[0] == "pop":
        print(s.pop())

