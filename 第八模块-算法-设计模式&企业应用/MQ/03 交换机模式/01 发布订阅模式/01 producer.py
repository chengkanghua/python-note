

import pika

# 链接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
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