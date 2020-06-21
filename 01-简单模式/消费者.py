#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 因为不确定是生产者先启动，还是消费者先启动
channel.queue_declare(queue='hello')


# 回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 告诉RabbitMQ这个回调函数从hello中的队列获取数据
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')

# 绑定RabbitMQ队列
channel.start_consuming()
