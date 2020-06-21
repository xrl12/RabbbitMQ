import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',  # 交换机模式
                      routing_key='hello',  # 队列名称
                      body='我真机智啊!',  # body消息内容
                      )
print(" [x] Sent 'Hello World!'")

connection.close()
