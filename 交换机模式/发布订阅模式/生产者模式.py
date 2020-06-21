from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建一个交换机
channel.exchange_declare(
    exchange='log',  # 交换机名字，可以随便写
    exchange_type='fanout'  # 什么模式的交换机，不可以随便写
)

message = 'info:A ask near your'
channel.basic_publish(
    exchange='log',
    body=message,
    routing_key='',
)

print(" [x] Sent %r" % message)
connection.close()
