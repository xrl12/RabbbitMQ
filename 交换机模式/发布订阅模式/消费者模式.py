from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建一个交换机
channel.exchange_declare(
    exchange='log',  # 交换机名字，可以随便写
    exchange_type='fanout'  # 什么模式的交换机，不可以随便写
)

# 创建一个队列
result = channel.queue_declare(
    queue='',
    exclusive=True  # 系统会随机生成一个名字
)
# 获取队列的名字
queue_name = result.method.queue
print('对列的名字：', queue_name)

# 将队列和交换机绑定起来
channel.queue_bind(
    exchange='log',
    queue=queue_name
)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print('接收到的数据是{}'.format(body))


channel.basic_consume(
    queue=queue_name,
    auto_ack=True,
    on_message_callback=callback
)

channel.start_consuming()
