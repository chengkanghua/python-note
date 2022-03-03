# ### 循环引用
# 基本案例
"""
import objgraph

class Person():
	pass

class Dog():
	pass

p = Person()
d = Dog()

print(objgraph.count("Person"))
print(objgraph.count("Dog"))

del p
del d
print(objgraph.count("Person"))
print(objgraph.count("Dog"))
"""
# 比较差异
import objgraph

class Person():
	pass

class Dog():
	pass

p = Person()
d = Dog()

print(objgraph.count("Person"))
print(objgraph.count("Dog"))

p.pet = d
d.master = p

del p
del d
print(objgraph.count("Person"))
print(objgraph.count("Dog"))

"""
1
1
1
1
"""




