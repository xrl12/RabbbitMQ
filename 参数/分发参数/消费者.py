from pika import ConnectionParameters, BlockingConnection

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()


"""
默认是轮询，不管你运行多慢，只要数据轮到你，就会给你分发数据。
使用公平分发，如果轮到你了，你接收的速度比下一个慢，就会把数据给下一个
"""
channel.queue_declare(
    queue='hello4'
)


def callback(ch, method, properties, body):
    print('接收到的参数{}'.format(body))


channel.basic_consume(
    queue='hello4',  # 接听的对列
    on_message_callback=callback  # 设置的回调函数
)
# 变成公平分发，谁接收数据的快，就将数据给谁
channel.basic_qos(prefetch_count=1)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
