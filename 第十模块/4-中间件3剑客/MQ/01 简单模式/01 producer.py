

import pika

# 1 链接rabbitmq
credentials = pika.PlainCredentials('root', 'root123')  # mq用户名和密码
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.6',port=5672,credentials=credentials))
channel = connection.channel()

# 2 创建队列
channel.queue_declare(queue='hello')

# 3 向指定队列插入数据
channel.basic_publish(exchange='', # 简单模式
                      routing_key='hello', # 指定队列
                      body='Hello Yuan!1111')

print(" [x] Sent 'Hello Yuan!'")