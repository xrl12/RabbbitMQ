from pika import ConnectionParameters, BlockingConnection

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建一个交换机
channel.exchange_declare(
    exchange='logs',
    exchange_type='direct',  # 指定交换机模式是关键字交换机
)

"""
给多个转换机发送
channel.basic_publish(
    exchange='logs',
    routing_key='info',
    body=message
)

channel.basic_publish(
    exchange='logs',
    routing_key='error',
    body=message
)

给单个转换机发送
channel.basic_publish(
    exchange='logs',
    routing_key='error',
    body=message
)
"""
message = 'info:This is very big BUG'
channel.basic_publish(
    exchange='logs',
    routing_key='info',
    body=message
)

# channel.basic_publish(
#     exchange='logs',
#     routing_key='error',
#     body=message
# )

# channel.basic_publish(
#     exchange='logs',
#     routing_key='warning',
#     body=message
# )

print('[*] This send message is {message}'.format(message=message))
connection.close()
