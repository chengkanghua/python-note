

def merge(li,left,mid,right):
    i = left
    j = mid+1
    ltmp = []
    while i <=mid and j <=right:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行完,肯定有一边没有数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= right:
        ltmp.append(li[j])
        j += 1
    li[left:right+1] = ltmp

def merge_sort(li,left,right):
    if left < right:
        mid = (left+right) // 2
        merge_sort(li,left,mid)   # 左边的数组
        merge_sort(li,mid+1,right) # 右边的数组
        merge(li,left,mid,right)

li = list(range(100))
import random
random.shuffle(li)
# print(li)
merge_sort(li, 0, len(li)-1)
print(li)

# ------------------------归并排序---算法分析
'''
1. 通过递归将一个大的数组一直分割,直到数组大小为1, 此时数组只有一个元素,就是有序的, 
然后把两个数组合并成一个2个元素的数组,在2和成4,直到合成一个数组


'''
# ------------------------归并排序---算法特性
'''
时间复杂度 o(nlogn)
空间复杂度 o(n)
'''