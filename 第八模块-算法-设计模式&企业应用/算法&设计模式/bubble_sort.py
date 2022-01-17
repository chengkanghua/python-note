
import random

# def bubble_sort(li):
#     for i in range(len(li)-1):
#         for j in range(len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j], li[j+1] = li[j+1],li[j]
#         print(li)
#
# li = [9,8,7,1,2,3,4,5,6]
# print(li)
# bubble_sort(li)


def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1],li[j]
                exchange = True
        print(li)
        if not exchange:
            return

li = [9,8,7,1,2,3,4,5,6]
print(li)

bubble_sort(li)