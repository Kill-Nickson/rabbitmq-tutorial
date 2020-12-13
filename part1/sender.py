import pika


with pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) as connection:
    channel = connection.channel()

    channel.queue_declare(queue='queue1')

    channel.basic_publish(exchange='',
                          routing_key='queue1',
                          body='Hello World!')

    print(" [x] Sent 'Hello World!'")
