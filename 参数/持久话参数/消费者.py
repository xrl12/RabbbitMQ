from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello2', durable=True)


def callback(ch, method, properties, body):
    print('消息的内容是{}'.format(body))


channel.basic_consume(
    queue='hello2',
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()