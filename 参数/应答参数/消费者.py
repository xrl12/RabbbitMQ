import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print('获取到的数据是{}'.format(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 告诉队列消息这个消息我处理完了，可以进行删除了


print(' [*] Waiting for messages. To exit press CTRL+C')

channel.basic_consume(
    queue='hello',
    auto_ack=False,  # 默认不应达
    on_message_callback=callback
)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
