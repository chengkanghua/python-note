'''
以尽可能多的方法解决2-sum问题并分析其时间复杂度：
给定一个列表和一个整数，从列表中找到两个数，使得两数之和等于给定的数，返回两个数的下标。题目保证有且只有一组解

'''


# def twoSum(nums,target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 if nums[i] +nums[j] == target:
#                     return [i,j]
#
# sums = [2,4,3,5,8,9]
# print(twoSum(sums,17))
# -----------------------------分析
'''
双层for循环,查找哪两个数相加结果等于target, 所以时间复杂度 o(n^2)

'''

def twoSum(nums,target):
    n = len(nums)
    for i in range(n):
        for j in range(i):
                if nums[i] +nums[j] == target:
                    return [i,j]

sums = [2,4,3,5,8,9]
print(twoSum(sums,17))

# ----------------------------分析
'''
外循环是遍历数组,内循环只遍历当前外循环指针前面的数, 
时间复杂度 o(nlogn)
'''




