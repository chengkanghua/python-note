from utils import Cal_time


@Cal_time
def linear_search(li,val):
    for ind,v in enumerate(li):
        if v == val:
            return ind
    else:
        return None

@Cal_time
def binary_search(li,val):
    left = 0
    right = len(li)-1
    while left <= right:  #候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: # 待查找的值在mid左侧
            right = mid - 1
        else: # li[mid] < val  待查找的值在mid右侧
            left = mid + 1
    else:
        return None

li = list(range(100000))
li2 = list(range(100000))
print(li)
# print(binary_search(li,3))
linear_search(li2,38900)
binary_search(li,38900)