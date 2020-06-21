import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 声明一个管道
channel = connection.channel()

# 声明queue，这个队列在RabbitMQ中生成，发送方和接收方使用同一个队列
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',  # 交换机模式
                      routing_key='hello',  # 队列名称
                      body='Hello world!',  # body消息内容
                      )
print(" [x] Sent 'Hello World!'")
connection.close()
