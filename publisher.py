import pika

# the 'requirements.txt' file is needed for this to work

# Access the CLODUAMQP_URL environment variable and parse it
params = pika.URLParameters('amqps://mhomznpp:jdDTdT3rqFFEsNtgL6XefLF8mlaTYIo8@goose.rmq2.cloudamqp.com/mhomznpp')
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel

channel.exchange_declare('test_exchange')
channel.queue_declare(queue='test_queue')
channel.queue_bind('test_queue', 'test_exchange', 'tests')

channel.basic_publish(
    body='Hello RabbitMQ',
    exchange='test_exchange',
    routing_key='tests'
)

channel.close()
connection.close()
