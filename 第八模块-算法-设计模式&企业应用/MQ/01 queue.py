

import queue


q=queue.Queue(maxsize=10) # FIFO

q.put(111)
q.put(222)
q.put(333)

print(q.get())
print(q.get())
print(q.get())
print(q.get())

