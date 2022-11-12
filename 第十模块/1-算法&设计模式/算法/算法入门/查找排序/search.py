# _*_coding:utf-8_*_
# created by Alex Li on 11/5/17

from cal_time import cal_time

# @cal_time
# def linear_search(li, val):
#     for ind, v in enumerate(li):
#         if v == val:
#             return ind
#     else:
#         return None

# @cal_time
# def binary_search(li, val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:    # 候选区有值
#         mid = (left + right) // 2
#         if li[mid] == val:
#             return mid
#         elif li[mid] > val: # 带查找的值在mid左侧
#             right = mid - 1
#         else: # li[mid] < val 带查找的值在mid右侧
#             left = mid + 1
#     else:
#         return None

# li = list(range(1000000))
# linear_search(li, 3890000)
# binary_search(li, 3890000)

@cal_time
def linear_search(li,val):
    for ind , v in enumerate(li):
        if v == val:
            return ind
    return None
@cal_time
def binary_search(li,val):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left + right) // 2
        if val == li[mid]:
            return mid
        elif li[mid] > val:
            right = mid-1
        else:
            left = mid-1
    return None

li = list(range(1000000))
linear_search(li,38900)
binary_search(li,38900)























