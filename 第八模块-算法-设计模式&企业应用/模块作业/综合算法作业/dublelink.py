'''

3. 封装一个双链表类，并实现双链表的创建、查找、插入和删除
'''

class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class doubleLinked(object):
    def __init__(self):
        self.head = Node()
        self.length = 0

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    # 对链表进行可迭代操作
    def iter_node(self):
        curnode = self.head.next
        while curnode.next != None:
            yield curnode
            curnode = curnode.next
        if curnode.next == None:
            yield curnode

    # 判断链表是否为空
    def is_Empty(self):
        return self.length == 0

    # 尾部添加
    def append(self, value):
        node = Node(value)
        if self.length == 0:
            node.prev = self.head
            self.head.next = node
        else:
            curnode = self.head.next
            while curnode.next != None:
                curnode = curnode.next
            curnode.next = node
            node.prev = curnode
        self.length += 1

    # 头部添加
    def add(self, value):
        if self.is_Empty():
            self.append(value)
        node = Node(value)
        curnode = self.head.next
        self.head.next = node
        node.next = curnode
        curnode.prev = node
        self.length += 1

    # 插入到指定位置
    def insert(self, postion, value):
        node = Node(value)
        curnode = self.head.next
        i = 2
        while i < postion:
            i += 1
            curnode = curnode.next
        node.next = curnode.next
        node.prev = curnode
        curnode.next.prev = node
        curnode.next = node
        self.length += 1
    # 删除表头节点
    def remove(self):
        if self.is_Empty():
            return False
        curnode = self.head.next
        self.head = self.head.next
        self.head.next = curnode.next
        self.length -= 1

    # 删除指定节点
    def delete(self, value):
        if self.is_Empty():
            return False
        curnode = self.head.next
        while curnode.value != value:
            curnode = curnode.next
        curnode.prev.next = curnode.next
        curnode.next.prev = curnode.prev
        curnode.next = curnode
        self.length -= 1



# 测试
linkedlist = doubleLinked()
print(linkedlist.is_Empty())
linkedlist.append(1)
linkedlist.append(3)
linkedlist.append(5)
linkedlist.add(4)
linkedlist.add(2)
linkedlist.insert(3,10)
# linkedlist.remove()
linkedlist.delete(3)
# 遍历打印
for i,node in enumerate(linkedlist):
    print("第%d个链表节点的值: %d"%(i+1, node))




