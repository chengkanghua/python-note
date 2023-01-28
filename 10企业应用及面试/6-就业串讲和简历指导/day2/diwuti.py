# ### 链表
# 1.创建链表
class Node():
	def __init__(self,value,next):
		self.value = value
		self.next = next


head = Node("头",None)
last = head

# 创建5个节点,形成一种链状的指向关系
for i in range(5):
	# 创建节点对象
	node = Node("d%s" % i , None) # d0 d1 d2 d3 d4
	# 把当前节点存在上一个节点的next属性中
	last.next = node
	# 把当前节点重置成上一个
	last = node

# 查看链表的关系
print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)
print(head.next.next.next.next.next.value)


# ### 2.链表的逆转
def reverse_link_list(head):

	# 要是空的,或者None 直接返回head
	if not head or not head.next:
		return head

	# 上一个节点对象
	prev_node = None
	# 下一个节点对象
	next_node = head.next
	# 当前节点对象
	current_node = head
	
	while True:
		# 修改next , 所指向的新的对象(存储上一个对象)
		current_node.next = prev_node
		
		if not next_node: # not None 已经是最后一个节点
			break
		
		# 重新获取上一个对象
		prev_node = current_node
		# 重新获取当前对象
		current_node = next_node
		# 重新获取下一个对象
		next_node = current_node.next
	
	return current_node
	
	
print("<=======>")
head = reverse_link_list(head)
print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)
print(head.next.next.next.next.next.value)



