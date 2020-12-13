import sys

import pika


with pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs',
                             exchange_type='direct',
                             durable=False,
                             auto_delete=False,
                             internal=False)

    severity = sys.argv[1]
    if severity is None:
        severity = 'info'

    message = ' '.join(sys.argv[2:])
    if message is []:
        message = 'Hello world'

    channel.basic_publish(exchange='direct_logs',
                          routing_key=severity,
                          body=message)

    print(f" [x] Sent {severity}: {message}")
