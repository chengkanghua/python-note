import struct
import os
# ########### 数值转换为固定4个字节，四个字节的范围 -2147483648 <= number <= 2147483647  ###########
v1 = struct.pack('i', 199)
# print(v1)  # b'\xc7\x00\x00\x00'
# print(type(v1))
# for item in v1:
#     print(item)

# # ########### 4个字节转换为数字 ###########
# v2 = struct.unpack('i', v1)  # v1= b'\xc7\x00\x00\x00'
# print(v2)  # (199,)

# v2 = struct.unpack('i',v1)
# print(v2[0])


print(os.sep)