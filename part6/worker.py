import pika


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def callback(ch, method, properties, body):
    n = int(body)
    print(f" [.] fib({n})")
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


with pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) as connection:
    channel = connection.channel()

    channel.queue_declare(queue='rpc_queue')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_message_callback=callback, queue='rpc_queue')

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()
