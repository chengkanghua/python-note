#_*_coding:utf-8_*_

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

'''
需求：

可依次选择进入各子菜单
可从任意一层往回退到上一层
可从任意一层退出程序

'''
# 保存进入的每一层记录
current_layer = menu
layers = []
while True:
    for k in current_layer:
        print(k)
    choice = input(">:").strip()
    if not choice:continue
    if choice in current_layer: # menu[北京]
        layers.append(current_layer)  # 进入下一层，保存当前层
        current_layer = current_layer[choice] # menu[北京][昌平]
    elif choice == 'b':
        if len(layers) != 0:
            current_layer = layers.pop()
        else:
            print("已经是顶层")
    elif choice == 'q':
        exit("bye.")






