from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建一个交换机
channel.exchange_declare(
    exchange='log3',
    exchange_type='topic'
)

# 往交换机里面插入数据
message = 'USA.weather is bad'
channel.basic_publish(
    exchange='log3',
    routing_key='usa.weather',
    body=message
)

print('Is send message is {message}'.format(message=message))

connection.close()
