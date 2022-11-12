import pika



# 链接rabbitmq
credentials = pika.PlainCredentials('root', 'root123')  # mq用户名和密码
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.6',port=5672,credentials=credentials))
channel = connection.channel()

# 声明一个名为logs类型为fanout的交换机
channel.exchange_declare(exchange='logs3',
                         exchange_type='topic')

# 创建队列
result = channel.queue_declare("",exclusive=True)
queue_name = result.method.queue
print(queue_name)

# 将指定队列绑定到交换机上
channel.queue_bind(exchange='logs3',
                   queue=queue_name,
                   routing_key="#.weather"
                   )


print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()