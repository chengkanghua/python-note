

import pika

# 1 链接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

# 2 创可持久化队列
channel.queue_declare(queue='hello4')

# 3 向指定队列插入数据
channel.basic_publish(exchange='', # 简单模式
                      routing_key='hello4', # 指定队列
                      body='Hello 999!',
                      )

