from pika import ConnectionParameters, BlockingConnection

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()

# 申明一个队列
channel.queue_declare(
    queue='hello4'
)

channel.basic_publish(
    routing_key='hello4',  # 发送的对列
    body='hello777',  # 发送的内容
    exchange='',  # 使用普通模式
)
