

import pika

# 链接rabbitmq
credentials = pika.PlainCredentials('root', 'root123')  # mq用户名和密码
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.6',port=5672,credentials=credentials))
channel = connection.channel()


# 声明一个名为logs类型为fanout的交换机
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout') # fanout：发布订阅模式参数

# 向logs交换机插入数据"info: Hello World!"
message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()