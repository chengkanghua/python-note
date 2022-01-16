maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 四个方向
dirs = [
    lambda x,y: (x+1,y),  # 左
    lambda x,y: (x-1,y),  # 右
    lambda x,y: (x,y-1),  # 上
    lambda x,y: (x,y+1),  # 下
]

def maze_path(x1,y1,x2,y2):
    '''

    :param x1: 起点位置  x
    :param y1: 起点位置  y
    :param x2: 目标位置  x
    :param y2: 目标位置  y
    :return:
    '''
    stack = []
    stack.append((x1,y1))
    while(len(stack) > 0):
        curNode = stack[-1] # 当前节点
        if curNode[0] == x2 and curNode[1] == y2:
            # 走到终点了
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 2表示已经走过
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print('没有路')
        return False

maze_path(1,1,8,8)

''' 使用栈解决迷宫问题
迷宫是一个定义好的二维数组,

按照起点位置, 循环 四个方向左右上下 方向走, 先判断所在位置是否是终点, 走过位置标记2,
并压入栈, 没有路回退,向其他方向走,
所有路回退没有可以走的表示没有路到达终点

'''
