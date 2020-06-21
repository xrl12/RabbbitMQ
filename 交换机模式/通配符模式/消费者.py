from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建要给交换机，防止他启动的比生产者快
channel.exchange_declare(
    exchange='log3',
    exchange_type='topic'
)

# 创建一个消息队列，和交换机进行绑定
result = channel.queue_declare(
    queue='',
    exclusive=True,  # 自动生成一个队列的名字
)

# 获取消息队列的名字
queue_name = result.method.queue

# 消息队列和交换机进行绑定
channel.queue_bind(
    queue=queue_name,
    exchange='log3',
    routing_key='usa.#'
)


# 回调函数
def callback(ch, method, properties, body):
    print('接收到的数据是{}'.format(body))


channel.basic_consume(
    queue=queue_name,
    auto_ack=True,
    on_message_callback=callback
)

channel.start_consuming()
