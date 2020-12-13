import sys
import time

import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode('utf-8')}")
    func_complexity = body.count(b'.')
    print(f" [x] Function will last for {func_complexity} seconds")
    time.sleep(func_complexity)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    with pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange='logs',
                                 exchange_type='fanout',
                                 durable=False,
                                 auto_delete=False,
                                 internal=False)

        channel.queue_declare(queue='',
                              passive=False,
                              durable=False,
                              exclusive=True,
                              auto_delete=False)

        channel.queue_bind('', 'logs')

        print(' [*] Waiting for messages. To exit press CTRL+C')

        channel.basic_consume('',
                              on_message_callback=callback,
                              auto_ack=False,
                              exclusive=True)

        channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
