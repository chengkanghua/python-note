# _*_coding:utf-8_*_
# created by Alex Li on 11/5/17
# 汉诺塔问题

# def hanoi(n, a, b, c):  # n表示几个盘子,  a 经过b  移动到c
#     if n>0:
#         hanoi(n-1, a, c, b)   # 第一步: n-1个盘子, a经过c移动到b
#         print("moving from %s to %s" % (a, c))  # 第二步: 从a移动到c
#         hanoi(n-1, b, a, c)                     # 第三步: 从b经过a移动到c
#
# hanoi(3, 'A', 'B', 'C')



def hanoi(n,a,b,c):
    if n > 0:
        hanoi(n-1,a,c,b)
        print("movie %s to %s" %(a,c))
        hanoi(n-1,b,a,c)

hanoi(3,"a","b","c")

















































