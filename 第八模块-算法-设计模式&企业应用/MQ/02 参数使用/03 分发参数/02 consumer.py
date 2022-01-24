import pika


credentials = pika.PlainCredentials('root', 'root123')  # mq用户名和密码
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.6',port=5672,credentials=credentials))
channel = connection.channel()

#  创建队列
channel.queue_declare(queue='hello4')


# 确定回调函数
def callback(ch, method, properties, body):
    import time
    time.sleep(3)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

#  公平分发（谁处理的快谁接收的多）  默认是轮询接收，
channel.basic_qos(prefetch_count=1)

# 确定监听队列参数
channel.basic_consume(queue='hello4',
                      auto_ack=False, # 默认应答改为手动应答
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式监听
channel.start_consuming()