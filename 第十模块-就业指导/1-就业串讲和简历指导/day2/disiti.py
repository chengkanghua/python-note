# ### 用两个队列实现一个栈
"""
栈: 先进后出, 后进先出
队列: 先进先出,后进后出
"""
from queue import Queue

class Stack():
	def __init__(self):
		self.master_queue = Queue()
		self.minor_queue = Queue()
		
		
	def push(self,val):
		# 入栈
		self.master_queue.put(val)
		
	
	def pop(self):
		# 出栈
		# 如果队列中没有任何值,直接返回None
		if self.master_queue.qsize() == 0:
			return None
		
		while True:
			# 当队列总长度为1的时候,循环终止,把最后一个元素取出来,为了满足栈的先进后出的特点;
			if self.master_queue.qsize() == 1:
				value = self.master_queue.get()
				break
			
			# 剩下还没有拿出来的元素,暂时放在2号队列中存储
			self.minor_queue.put(self.master_queue.get())
			
			
			
		# 交换队列,重新循环,继续找最后一个值,依次类推
		self.master_queue , self.minor_queue = self.minor_queue , self.master_queue
		return value
		
obj = Stack()
obj.push("1")
obj.push("2")	
obj.push("3")	

print(obj.pop())
print(obj.pop())			
print(obj.pop())			
print(obj.pop())			
			
			
			