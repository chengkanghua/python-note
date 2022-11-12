



import requests




# response = requests.request(method='get', url='https://www.autohome.com.cn/news/')
response = requests.get('https://www.autohome.com.cn/news/')
# print(response)  # 查看响应状态
print(response.status_code)  # 查看响应状态
# print(response.content)  # 查看bytes类型的数据，通常是获取图片
# print(response.headers)   # 查看响应头
# print(response.json())   # 获取json类型的数据，要确保响应类型是json，不然报错
# response.encoding = "GBK"   # 指定(修改)当前响应结果的编码类型
# print(response.text)   # 文本类型的数据用text
# print(response.content)  # 获取bytes类型的数据
# print(response.url)  # 当前请求的url
# print(response.encoding)  # 获取当前响应的编码类型
# print(response.request)  # 请求类型
# print(response.request.method)  # 请求类型
# print(response.cookies)  # 查看cookis
# print(response.is_redirect)  # 查看是否是重定向的响应
# print(response.iter_lines())  # 循环获取，一行一行的取，但是，请忘掉这个方法
# print(response.iter_content(chunk_size=1024))  # 迭代取值，可以指定chunk_size
# print(response.reason)









