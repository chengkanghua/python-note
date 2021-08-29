# 基于列表推导式一行实现输出9*9乘法表。


data = '\n'.join([" ".join(['{}*{}={}'.format(i,j,i*j) for i in range(1,j+1)]) for j in range(1,10)])
print(data)

data2 ="\n".join([" ".join(['{}*{}'.format(i, j) for j in range(1, i + 1)]) for i in range(1, 10)])
# print(data2)
# [" ".join(['{}*{}'.format(i, j) for j in range(1, i + 1)]) for i in range(1, 10)]
#          ['{}*{}'.format(i, j) for j in range(1, i + 1)]

data3 = [" ".join(['{}*{}'.format(i, j) for j in range(1, i + 1)]) for i in range(1, 10)]
print(data3)

data4 = '\n'.join([" ".join(['{}*{}'.format(i, j) for j in range(1, i + 1)]) for i in range(1,10)])
print(data4)
