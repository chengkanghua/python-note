'''
5. 使用动态规划算法实现最长公共子序列问题
'''

def lcs_length(x,y):
    m = len(x)
    n = len(y)
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for row in range(1,m+1):
        for col in range(1,n+1):
            if table[row-1] == table[col-1]:
                table[row][col] = table[row-1][col-1]+1
            else:
                table[row][col] = max(table[row][col-1],table[row-1][col])
    for _ in table:
        print(_)
    return table[m][n]


result = lcs_length('ABCBDAB','BDCABA')
print(result)

# ----------------------------------最长公共子序列
'''
给两个字符串求出最长公共子序列数?

1 基于两个字符串生成一个二维数组, 第一行与第一列追加一个0
2 在表格上用计算公式填写数字
    公式: 纵向字符和横向字符相等的情况下, 用左上角的数字+1 ,不相等就取左边和上边的最大值.

扩展视频:
https://www.bilibili.com/video/BV1S3411e7C8
https://www.bilibili.com/video/BV14A411v7mP
'''

