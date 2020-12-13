import pika


with pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) as connection:
    channel = connection.channel()

    channel.queue_declare(queue='queue2', durable=True)

    message = '. . .'
    channel.basic_publish(exchange='',
                          routing_key='queue2',
                          body=message,
                          properties=pika.BasicProperties(delivery_mode=2,))

    print(f" [x] Sent {message}")
