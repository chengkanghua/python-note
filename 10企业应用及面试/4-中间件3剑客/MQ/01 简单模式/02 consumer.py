import pika

credentials = pika.PlainCredentials('root', 'root123')  # mq用户名和密码
connection = pika.BlockingConnection(pika.ConnectionParameters('10.211.55.6',credentials=credentials))
channel = connection.channel()

#  创建队列
channel.queue_declare(queue='hello')


# 确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# 确定监听队列参数
channel.basic_consume(queue='hello',
                      auto_ack=True, # 默认应答  消息队列中取走了，消息队列中就没有了
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式监听
channel.start_consuming()