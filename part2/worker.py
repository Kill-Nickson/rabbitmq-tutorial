import sys
import time

import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    func_complexity = body.count(b'.')
    print(f" [x] Function will last for {func_complexity} seconds")
    time.sleep(func_complexity)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    with pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='queue2', durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='queue2',
                              on_message_callback=callback,
                              auto_ack=False,
                              exclusive=False,
                              consumer_tag=None,
                              arguments=None)

        channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
