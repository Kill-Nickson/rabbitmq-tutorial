import pika

with pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='logs',
                             exchange_type='fanout',
                             durable=False,
                             auto_delete=False,
                             internal=False)
    queues_list = list()
    queues_list.append(channel.queue_declare(queue='',
                                             passive=False,
                                             durable=False,
                                             exclusive=True,
                                             auto_delete=False))

    message = b'. . .'
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=message,
                          properties=pika.BasicProperties(delivery_mode=2, ))

    print(f" [x] Sent {message}")
