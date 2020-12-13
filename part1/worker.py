import sys

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))


def main():
    with pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='queue1')
        print(' [*] Waiting for messages. To exit press CTRL+C')

        channel.basic_consume(queue='queue1',
                              on_message_callback=callback,
                              auto_ack=True,
                              exclusive=False,
                              consumer_tag=None,
                              arguments=None)

        channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
