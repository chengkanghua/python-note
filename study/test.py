import string
import itertools

# 生成 0-9 A-z 列表
print(string.digits)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
#方法一
# data = []
# for i in string.digits:
#     data.append(i)
# for i in string.ascii_uppercase:
#     data.append(i)
# for i in string.ascii_lowercase:
#     data.append(i)
# print(data)
#方法二
# data = [item for item in itertools.chain(string.digits,string.ascii_uppercase,string.ascii_lowercase)]
# print(data)
#方法三
data = list(itertools.chain(string.digits, string.ascii_uppercase, string.ascii_lowercase))

def base62encode(num: int):
    count_num = len(data)
    postion_value = []
    while num >= count_num:
        num,remain = divmod(num,count_num)
        postion_value.insert(0,data[remain])
    postion_value.insert(0,data[num])
    result = ''.join(postion_value)
    return result

print(base62encode(2222312))
print(base62encode(3011))
print(base62encode(5011111))



