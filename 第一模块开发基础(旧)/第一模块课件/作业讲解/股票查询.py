f = open("stock_data.txt", "r", encoding="utf-8")
query_columns = ["最新价", "涨跌幅", "换手率"]
columns = f.readline().strip().split(',')
# print(columns) # ['序号', '代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量(手)', '成交额', '振幅', '最高', '最低', '今开', '昨收', '量比', '换手率', '市盈率', '市净率']
stock_data = {}

for line in f:
    line = line.strip().split(',')
    name = line[2]
    stock_data[name] = line  # 创建股票数据dict{name：data...}

while True:
    count = 0
    cmd = input("输入查询指令>>:").strip()
    if len(cmd) == 0:
        continue
    print(columns)
    for s_name in stock_data:
        if cmd in s_name:
            print(stock_data[s_name])
            count += 1

    if ">" in cmd:
        q_name, q_val = cmd.split('>')
        q_name = q_name.strip()
        q_val = float(q_val)
        if q_name in query_columns:  # 输入的name 在查询列表里
            q_name_index = columns.index(q_name)
            for s_name, s_vals in stock_data.items():
                if float(s_vals[q_name_index].strip('%')) > q_val:
                    print(s_vals)
                    count += 1
    elif "<" in cmd:
        pass
    if count > 0:
        print("匹配到%s条" % count)

    # else: # 当输入不为空时
    #     query_name_list = query_name.strip().split(">"or'<')
    #     if len(query_name_list) == 1: # 当输入只为name时
    #         print(first_cross)
    #         for k in stock_data:
    #             if query_name in k:
    #                 count += 1
    #                 print(k,stock_data[k])
    #
    #             print("相似信息共找到%d条" % count)
    #             break
    #         else:
    #                 print("未找到相关信息，请重新输入")
    #                 break
