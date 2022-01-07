
# 快速排序

def partition(li,left,right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >=tmp: # 从右面找到比tmp小的数
            right -= 1       # 往左走一步
        li[left] = li[right]
    li[left] = tmp

