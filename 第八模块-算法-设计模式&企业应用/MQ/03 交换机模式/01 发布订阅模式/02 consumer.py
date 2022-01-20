import pika



# 链接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明一个名为logs类型为fanout的交换机
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# 创建队列
result = channel.queue_declare("",exclusive=True)
queue_name = result.method.queue
print(queue_name)

# 将指定队列绑定到交换机上
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()