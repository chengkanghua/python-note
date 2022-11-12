# -*- coding:utf-8 -*-
import os

# print("计算1~20内的两数之和，包含1和20")

def add(x, y):
    return int(x) + int(y)

while True:
    try:
        num1 = input('请输入一个值或输入 q 退出: ').strip()
        if num1.upper() == 'Q':
            break
        num2 = input('再次输入一个值: ').strip()
        os.system('cls')
        print('{} + {} = {}'.format(num1, num2, add(num1, num2)))
    except Exception as e:
        print(e)