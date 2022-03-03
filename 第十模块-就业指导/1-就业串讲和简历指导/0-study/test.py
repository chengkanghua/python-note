ip = "10.3.9.12"
strvar = ""
for i in ip.split("."):
    bin_str = str(bin(int(i)))[2:]
    print(bin_str)
    # 补8位,不够8位的拿0来补位
    strvar += bin_str.rjust(8, "0")
print(strvar)
# # 把二进制字符串转换成十进制(默认)
print(int(strvar,2))
