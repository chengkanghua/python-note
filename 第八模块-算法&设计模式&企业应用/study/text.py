

# def func3(x):
#     if x > 0:
#         print(x)
#         func3(x-1)
#
# func3(3)

def func4(x):
    if x > 0:
        func4(x-1) # 3 2 1 --> 1 2 3
        print(x)



