class Node:
    def __init__(self, item):
        self.item = item
        self.next = None  # 初始节点的next节点为None


class OperatorLinkList(object):
    """ 单向链表的操作 """

    def create_link_list_head(self, li):
        """ 头插法，这里可以不管tail，因为tail一直不变 """
        head = Node(li[0])  # 将列表下标为0的元素当作head
        for element in li[1:]:  # 因为下标为0的元素已经被当作头节点了，所以这里从下标1开始循环
            node = Node(element)  # 创建新的节点
            node.next = head  # 将新节点的next指向上个节点
            head = node  # 然后将head指向新节点
        return head  # 返回链表的head，可以通过head找到链表中的所有节点

    def create_link_list_tail(self, li):
        """ 尾插法，这里可以不管head，因为head一直不变 """
        head = Node(li[0])  # 将列表下标为0的元素当作head
        tail = head  # 刚开始，尾巴和head都指向头节点
        for element in li[1:]:
            node = Node(element)  # 创建新的节点
            tail.next = node  # 让当前节点的next指向新节点
            tail = node  # 让tail也指向新节点
        return head  # 返回链表的head，可以通过head找到链表中的所有节点

    def get_link_list(self, head):
        """ 通过head获取链表的所有节点 """
        while head:  # 当head.next不为None，就循环输出
            print(head.item, end=' ')
            head = head.next
        print()

    def insert_node(self, head, key, element):
        """ 插入，head是链表的头部，key表示插入的位置，element插入的元素 """
        p = Node(element)
        while head:
            if head.item == key:
                p.next = head.next
                head.next = p
            head = head.next  # 用于循环，从head挨个往后找，直到遇到None

    def remove_node(self, head, element):
        """ 删除节点，head是链表的头部，element是要删除的元素 """
        while head:
            # 如果当前元素的下一个节点值等于element，那就让当前节点next指向下一个节点的下一个节点
            if head.next.item == element:
                head.next = head.next.next
                break
            head = head.next
        else:
            print('删除的元素[{}]不存在'.format(element))


lk = OperatorLinkList()
h = lk.create_link_list_head([1, 2, 3])  # 头插法创建单向链表
t = lk.create_link_list_tail([1, 2, 3])  # 尾插法创建单向链表
lk.get_link_list(t)
lk.insert_node(t, 1, 4)
lk.get_link_list(t)
lk.remove_node(t, 2)
lk.get_link_list(t)

lk.get_link_list(h)
