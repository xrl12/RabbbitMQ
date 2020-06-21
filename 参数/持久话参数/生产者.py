from pika import BlockingConnection, ConnectionParameters, BasicProperties

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello2', durable=True)  # durable：把数据变成可持久话

channel.basic_publish(
    exchange='',
    body='Hello World!',
    routing_key='hello2',  # 队列名称
    properties=BasicProperties(
        delivery_mode=2,  # 让里面的消息变得可持久话
    )
)

connection.close()
