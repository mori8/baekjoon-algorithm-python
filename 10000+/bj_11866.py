class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node('head')
        self.head.next = self.head  # 원형 연결 리스트의 특징

    def find(self, item):
        cur_node = self.head
        while cur_node.element != item:
            cur_node = cur_node.next
        return cur_node

    def insert(self, newItem, prevItem):
        new_node = Node(newItem)
        cur_node = self.find(prevItem)
        new_node.next = cur_node.next
        cur_node.next = new_node

    def show(self):
        cur_node = self.head
        while cur_node.next.element is not 'head':
            print(cur_node.element, end='->')
            cur_node = cur_node.next
        print(cur_node.element)

    def find_previous(self, item):
        cur_node = self.head
        while (cur_node.next is not None) and (cur_node.next.element != item):
            cur_node = cur_node.next
        return cur_node

    def remove(self, item):
        prev_node = self.find_previous(item)
        if prev_node is not None:
            prev_node.next = prev_node.next.next


n, k = map(int, input().split())
c = CircularLinkedList()
ansList = []

c.insert(1, 'head')

if n != 1:
    for i in range(2, n+1):
        c.insert(i, i-1)

del_node = c.find(k)

while c.head.next != c.head:
    ansList.append(del_node.element)
    c.remove(del_node.element)
    for i in range(k):
        if del_node.next.element is 'head':
            del_node = del_node.next.next
        else:
            del_node = del_node.next

print("<", end='')
print(", ".join(map(str, ansList)),end='')
print(">", end='')
