
import random
def partition(li,left,right):
    mid = li[left]
    while left < right:
        while left < right and li[right] >= mid:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= mid:
            left += 1
        li[right] = li[left]
    li[left] = mid
    return mid

def quick_sort(li,left,right):
    if left < right:
        mid = partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

li = list(range(100))
random.shuffle(li)
print(li)
quick_sort(li,0,len(li)-1)
print(li)

# ---------------------------------算法解析
'''
1 从数组中取的第一个元素,作为中轴元素, 把所有大于中轴的数放入右边,把小于中轴的数放入左边,
显然,此时中轴元素的位置是有序的,
2 把中轴左边和右边的数组(不包括中轴元素)都分成两个小数组,继续第一步的操作, 直到数组的大小为1.此时每个元素都处于有序位置. 
'''
# ---------------------------------算法特性
'''
时间复杂度 o(nlogn)
空间复杂度 o(logn)
'''





