from pika import ConnectionParameters, BlockingConnection

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='direct'
)

# 创建一个消息队列
result = channel.queue_declare(
    queue='',
    exclusive=True
)
queue_name = result.method.queue
print('This exchange name is {name}'.format(name=queue_name))

# 将交换机和消息队列绑定起来
"""
绑定单个消息队列
channel.queue_bind(
    queue=queue_name,
    exchange='logs',
    routing_key='info',  # 直接这个关键字的消息
)

绑定多个消息队列
channel.queue_bind(
    queue=queue_name,
    exchange='logs',
    routing_key='info',  # 直接这个关键字的消息
)

channel.queue_bind(
    queue=queue_name,
    exchange='logs',
    routing_key='error',  # 直接这个关键字的消息
)

channel.queue_bind(
    queue=queue_name,
    exchange='logs',
    routing_key='warings',  # 只接收这个关键字的消息
)
"""
channel.queue_bind(
    queue=queue_name,
    exchange='logs',
    routing_key='info',  # 只接收这个关键字的消息
)

# channel.queue_bind(
#     queue=queue_name,
#     exchange='logs',
#     routing_key='error'
# )

# channel.queue_bind(
#     queue=queue_name,
#     exchange='logs',
#     routing_key='warning'
# )


def callback(ch, method, properties, body):
    print('接收到的数据是{}'.format(body))


# 获取那个消息对列的数据
channel.basic_consume(
    queue=queue_name,
    auto_ack=True,
    on_message_callback=callback,
)

channel.start_consuming()
